/**
 * SynapseDesk AI - Spatial Panel System
 * Manages reactive UIKitML event bindings across all three cockpit panels.
 */

import { createSystem, UIKitMLAsset, VisibilityState } from '@iwsdk/core';
import { agentEngine } from './agent.js';
import { sound } from './audio.js';

export class PanelSystem extends createSystem({}) {
  init(): void {
    // 1. Central Hub Panel
    const hubPanel = this.world.getSceneObject<UIKitMLAsset>('synapse-hub');
    const intentPanel = this.world.getSceneObject<UIKitMLAsset>('synapse-intent');
    const agentPanel = this.world.getSceneObject<UIKitMLAsset>('synapse-agent');

    // XR Buttons (Hub)
    const xrButton = hubPanel?.getElementById('xr-button');
    const exitButton = hubPanel?.getElementById('exit-button');

    if (xrButton && exitButton) {
      if (!this.world.xrEnabled) {
        xrButton.setProperties({ display: 'none' });
        exitButton.setProperties({ display: 'none' });
      } else {
        const launchXR = () => this.world.launchXR();
        const exitXR = () => this.world.exitXR();
        xrButton.addEventListener('click', launchXR);
        exitButton.addEventListener('click', exitXR);

        this.cleanupFuncs.push(
          () => xrButton.removeEventListener('click', launchXR),
          () => exitButton.removeEventListener('click', exitXR),
          this.world.visibilityState.subscribe((visibilityState) => {
            const is2D = visibilityState === VisibilityState.NonImmersive;
            xrButton.setProperties({ display: is2D ? 'flex' : 'none' });
            exitButton.setProperties({ display: is2D ? 'none' : 'flex' });
          }),
        );
      }
    }

    // Hub Interactive Actions
    const btnAutoCluster = hubPanel?.getElementById('btn-autocluster');
    if (btnAutoCluster) {
      btnAutoCluster.addEventListener('click', () => {
        sound.playSynthesis();
        agentEngine.autoClusterNodes();
        this.updateAgentTelemetry(agentPanel);
      });
    }

    const btnSynthesize = hubPanel?.getElementById('btn-synthesize');
    if (btnSynthesize) {
      btnSynthesize.addEventListener('click', () => {
        sound.playSynthesis();
        agentEngine.decomposeIntent(agentEngine.getIntent());
        this.updateAgentTelemetry(agentPanel);
      });
    }

    // Task Completion Buttons
    ['btn-done-1', 'btn-done-2', 'btn-done-3'].forEach((btnId, idx) => {
      const btn = hubPanel?.getElementById(btnId);
      if (btn) {
        btn.addEventListener('click', () => {
          sound.playDone();
          agentEngine.completeTask(idx);
          btn.setProperties({ display: 'none' });
          this.updateAgentTelemetry(agentPanel);
        });
      }
    });

    // Sprint Mode Timer
    const btnTimerToggle = hubPanel?.getElementById('btn-timer-toggle');
    const btnTimerLabel = hubPanel?.getElementById('btn-timer-label');
    const sprintTimerText = hubPanel?.getElementById('sprint-timer');

    if (btnTimerToggle) {
      btnTimerToggle.addEventListener('click', () => {
        sound.playPinch();
        agentEngine.toggleSprintTimer((formattedTime, isRunning) => {
          if (sprintTimerText) {
            // Text updates in UIKitML
            sprintTimerText.setProperties({ text: formattedTime });
          }
          if (btnTimerLabel) {
            btnTimerLabel.setProperties({ text: isRunning ? 'Pause' : 'Start' });
          }
          if (formattedTime === '00:00') {
            sound.playDone();
          }
        });
      });
    }

    // Left Panel: Intent Preset Buttons
    const intentTextEl = intentPanel?.getElementById('current-intent-text');
    const presets: Record<string, string> = {
      'btn-preset-vr': 'Architect and ship Meta VR Start Competition submission with hands-first 60 FPS compliance.',
      'btn-preset-exam': 'Master Quantum Computing qubit rotations and error correction surface codes.',
      'btn-preset-opt': 'Optimize Meta Quest mobile GPU pipeline: foveated rendering, draw call batching, Havok physics.',
    };

    Object.entries(presets).forEach(([btnId, promptText]) => {
      const presetBtn = intentPanel?.getElementById(btnId);
      if (presetBtn) {
        presetBtn.addEventListener('click', () => {
          sound.playSynthesis();
          agentEngine.setIntent(promptText);
          if (intentTextEl) {
            intentTextEl.setProperties({ text: `"${promptText}"` });
          }
          this.updateAgentTelemetry(agentPanel);
        });
      }
    });

    // Right Panel: Export Structured Plan
    const btnExport = agentPanel?.getElementById('btn-export-audit');
    if (btnExport) {
      btnExport.addEventListener('click', () => {
        sound.playDone();
        const telemetry = agentEngine.getTelemetry();
        const exportData = {
          protocol: 'SynapseDesk AI Spatial Autonomous Cognition',
          intent: agentEngine.getIntent(),
          nodes: agentEngine.getNodes(),
          telemetry,
          exportedAt: new Date().toISOString(),
        };
        console.log('[SYNAPSE EXPORT PLAN]', JSON.stringify(exportData, null, 2));
        agentEngine.addLog('[EXPORT] Structured action plan output to browser console/telemetry.');
        this.updateAgentTelemetry(agentPanel);
      });
    }
  }

  private updateAgentTelemetry(agentPanel: UIKitMLAsset | undefined): void {
    if (!agentPanel) return;
    const telemetry = agentEngine.getTelemetry();
    const loadEl = agentPanel.getElementById('cognitive-load-val');
    const logEl = agentPanel.getElementById('latest-agent-log');

    if (loadEl) {
      loadEl.setProperties({ text: `${telemetry.cognitiveLoadPct}% (${telemetry.flowState.toUpperCase()})` });
    }
    if (logEl && telemetry.logs[0]) {
      logEl.setProperties({ text: `> ${telemetry.logs[0]}` });
    }
  }
}
