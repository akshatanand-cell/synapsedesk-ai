/**
 * SynapseDesk AI - 3D Spatial Agent Entity & Interactive Task Prisms
 * Implements the floating Synapse Core agent and grabbable 3D cognitive nodes.
 */

import {
  createComponent,
  createSystem,
  DistanceGrabbable,
  Group,
  Hovered,
  IcosahedronGeometry,
  Mesh,
  MeshPhysicalMaterial,
  MeshStandardMaterial,
  OctahedronGeometry,
  OneHandGrabbable,
  PokeInteractable,
  Pressed,
  RayInteractable,
  TorusGeometry,
  Vector3,
} from '@iwsdk/core';
import { agentEngine } from './agent.js';
import { sound } from './audio.js';

export const SynapseCoreTag = createComponent('SynapseCoreTag', {});
export const SpatialNodeTag = createComponent('SpatialNodeTag', {
  nodeIndex: { type: 'number', default: 0 },
});

export class SynapseCoreSystem extends createSystem({
  cores: { required: [SynapseCoreTag] },
  nodes: { required: [SpatialNodeTag] },
  pressedCore: { required: [SynapseCoreTag, Pressed] },
  pressedNode: { required: [SpatialNodeTag, Pressed] },
  hoveredNode: { required: [SpatialNodeTag, Hovered] },
}) {
  private tempVec = new Vector3();
  private coreGroup: Group | null = null;
  private ringMesh: Mesh | null = null;
  private orbMesh: Mesh | null = null;
  private nodeEntities: Array<{ mesh: Mesh; index: number }> = [];

  init(): void {
    // 1. Create the floating Synapse Core Agent Entity
    const coreEntity = this.world.createEntity();
    this.coreGroup = new Group();
    this.coreGroup.position.set(0, 1.35, -0.62);

    // Glowing Holographic Core (Icosahedron)
    const orbGeo = new IcosahedronGeometry(0.048, 1);
    const orbMat = new MeshPhysicalMaterial({
      color: 0x38bdf8,
      emissive: 0x0284c7,
      emissiveIntensity: 0.8,
      roughness: 0.1,
      metalness: 0.2,
      transmission: 0.6,
      transparent: true,
      opacity: 0.9,
    });
    this.orbMesh = new Mesh(orbGeo, orbMat);
    this.coreGroup.add(this.orbMesh);

    // Outer Orbiting Halo Ring
    const ringGeo = new TorusGeometry(0.075, 0.003, 16, 48);
    const ringMat = new MeshStandardMaterial({
      color: 0xa855f7,
      emissive: 0x7e22ce,
      emissiveIntensity: 0.7,
      metalness: 0.8,
      roughness: 0.2,
    });
    this.ringMesh = new Mesh(ringGeo, ringMat);
    this.ringMesh.rotation.x = Math.PI / 3;
    this.coreGroup.add(this.ringMesh);

    coreEntity.object3D = this.coreGroup;
    coreEntity.addComponent(SynapseCoreTag);
    coreEntity.addComponent(RayInteractable);
    coreEntity.addComponent(PokeInteractable);

    // 2. Create the 3 Grabbable Hands-First Spatial Task Prisms
    const taskColors = [0xef4444, 0x38bdf8, 0x10b981]; // Red (Urgent), Cyan (Strategy), Green (AI)

    for (let i = 0; i < 3; i++) {
      const nodeEntity = this.world.createEntity();
      const nodeGeo = new OctahedronGeometry(0.032, 0);
      const nodeMat = new MeshPhysicalMaterial({
        color: taskColors[i % taskColors.length],
        emissive: taskColors[i % taskColors.length],
        emissiveIntensity: 0.4,
        roughness: 0.2,
        metalness: 0.5,
        clearcoat: 1.0,
      });

      const mesh = new Mesh(nodeGeo, nodeMat);
      // Position along the seated 2ft curved arc
      const angle = (i - 1) * 0.28;
      const x = Math.sin(angle) * 0.52;
      const z = -Math.cos(angle) * 0.52;
      const y = 0.98 + (i % 2 === 0 ? 0.02 : -0.02);
      mesh.position.set(x, y, z);

      nodeEntity.object3D = mesh;
      nodeEntity.addComponent(SpatialNodeTag, { nodeIndex: i });
      nodeEntity.addComponent(RayInteractable);
      nodeEntity.addComponent(PokeInteractable);
      nodeEntity.addComponent(OneHandGrabbable);
      nodeEntity.addComponent(DistanceGrabbable);

      this.nodeEntities.push({ mesh, index: i });
    }

    // Interaction triggers
    this.queries.pressedCore.subscribe('qualify', () => {
      sound.playSynthesis();
      agentEngine.autoClusterNodes();
      if (this.orbMesh) {
        (this.orbMesh.material as MeshPhysicalMaterial).emissiveIntensity = 2.0;
        setTimeout(() => {
          if (this.orbMesh) {
            (this.orbMesh.material as MeshPhysicalMaterial).emissiveIntensity = 0.8;
          }
        }, 400);
      }
    });

    this.queries.pressedNode.subscribe('qualify', () => {
      sound.playPinch();
    });

    this.queries.hoveredNode.subscribe('qualify', (entity) => {
      sound.playPinch();
      const mesh = entity.object3D as Mesh;
      if (mesh && mesh.material) {
        (mesh.material as MeshPhysicalMaterial).emissiveIntensity = 1.0;
      }
    });

    this.queries.hoveredNode.subscribe('disqualify', (entity) => {
      const mesh = entity.object3D as Mesh;
      if (mesh && mesh.material) {
        (mesh.material as MeshPhysicalMaterial).emissiveIntensity = 0.4;
      }
    });
  }

  update(delta: number, time: number): void {
    // Animate Synapse Core Agent: gentle rotation and hovering
    if (this.orbMesh) {
      this.orbMesh.rotation.y += delta * 0.8;
      this.orbMesh.rotation.x += delta * 0.4;
      this.orbMesh.position.y = Math.sin(time * 2.2) * 0.012;
    }
    if (this.ringMesh) {
      this.ringMesh.rotation.z += delta * 1.2;
      this.ringMesh.rotation.y += delta * 0.6;
    }

    // Smoothly animate task prisms toward their auto-clustered target positions
    const nodesData = agentEngine.getNodes();
    this.nodeEntities.forEach(({ mesh, index }) => {
      const data = nodesData[index];
      if (data && mesh) {
        // If the task was marked completed, float it up and fade slightly
        if (data.status === 'completed') {
          mesh.position.y += delta * 0.04;
          (mesh.material as MeshPhysicalMaterial).opacity = 0.4;
          (mesh.material as MeshPhysicalMaterial).transparent = true;
        } else {
          // Softly lerp toward target position
          this.tempVec.set(data.targetPosition[0], data.targetPosition[1], data.targetPosition[2]);
          mesh.position.lerp(this.tempVec, delta * 3.5);
          mesh.rotation.y += delta * 0.9;
        }
      }
    });
  }
}
