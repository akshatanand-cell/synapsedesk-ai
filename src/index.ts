/**
 * SynapseDesk AI - Autonomous Spatial Workspace
 * Entry Point
 */

import { World } from '@iwsdk/core';
import projectOptions from 'virtual:iwsdk-project';
import { PanelSystem } from './panel.js';
import { RobotSystem } from './robot.js';
import { SynapseCoreSystem } from './synapse-core.js';

World.create(
  document.getElementById('scene-container') as HTMLDivElement,
  projectOptions,
).then((world) => {
  world.registerSystem(RobotSystem);
  world.registerSystem(SynapseCoreSystem);
  world.registerSystem(PanelSystem);
  console.log('[SYNAPSE DESK AI] Initialized in Seated 2-Foot Spatial Envelope.');
});
