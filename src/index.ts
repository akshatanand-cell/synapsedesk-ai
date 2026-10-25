/**
 * SynapseDesk AI - Autonomous Spatial Workspace
 * Entry Point
 */

import { World, launchXR } from '@iwsdk/core';
import { AmbientLight, DirectionalLight, Vector3 } from 'three';
import projectOptions from 'virtual:iwsdk-project';
import { PanelSystem } from './panel.js';
import { RobotSystem } from './robot.js';
import { SynapseCoreSystem } from './synapse-core.js';

let activeWorld: any = null;

export async function enterVR() {
  if (activeWorld) {
    if (navigator.xr) {
      try {
        const isSupported = await navigator.xr.isSessionSupported('immersive-vr');
        if (isSupported) {
          launchXR(activeWorld);
          return { success: true };
        }
      } catch (e) {
        console.warn('[SynapseDesk] XR query warning:', e);
      }
    }
    return {
      success: false,
      reason: 'No WebXR headset detected in this browser. To experience hands-first 3D interaction, open this URL inside Meta Quest Browser.',
    };
  }
  return { success: false, reason: 'Spatial engine is initializing...' };
}

(window as any).enterSynapseVR = enterVR;

World.create(
  document.getElementById('scene-container') as HTMLDivElement,
  projectOptions,
).then((world) => {
  activeWorld = world;
  (window as any).__SYNAPSE_WORLD__ = world;

  // Add rich spatial cockpit lighting
  const ambientLight = new AmbientLight(0xffffff, 1.8);
  world.scene.add(ambientLight);
  const cyanKeyLight = new DirectionalLight(0x38bdf8, 2.5);
  cyanKeyLight.position.set(1.5, 3.0, 2.0);
  world.scene.add(cyanKeyLight);
  const purpleFillLight = new DirectionalLight(0xa855f7, 1.5);
  purpleFillLight.position.set(-1.5, 2.0, 1.0);
  world.scene.add(purpleFillLight);

  // Position browser camera directly in seated user eye-line
  if (world.camera) {
    world.camera.position.set(0, 1.25, 0.05);
    world.camera.lookAt(new Vector3(0, 1.15, -0.65));
  }

  world.registerSystem(RobotSystem);
  world.registerSystem(SynapseCoreSystem);
  world.registerSystem(PanelSystem);
  console.log('[SYNAPSE DESK AI] Initialized in Seated 2-Foot Spatial Envelope.');
  window.dispatchEvent(new CustomEvent('synapse:ready', { detail: { world } }));
});
