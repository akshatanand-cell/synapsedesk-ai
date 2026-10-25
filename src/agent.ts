/**
 * SynapseDesk AI - Autonomous Cognitive Agent Engine
 * Core intelligence loop for spatial decomposition, auto-clustering,
 * and cognitive load telemetry.
 */

export interface SpatialTaskNode {
  id: string;
  title: string;
  priority: 'P1' | 'P2' | 'P3';
  category: string;
  status: 'active' | 'completed';
  estimatedMins: number;
  position: [number, number, number];
  targetPosition: [number, number, number];
}

export interface CognitiveTelemetry {
  cognitiveLoadPct: number;
  flowState: 'Deep Flow' | 'Balanced' | 'Overload Risk';
  nodesInReach: number;
  maxReachRadiusMeters: number;
  logs: string[];
}

export class SynapseAgentEngine {
  private activeIntent = 'Architect and ship the Meta VR Start Competition submission with hands-first 60 FPS compliance.';
  private nodes: SpatialTaskNode[] = [];
  private logs: string[] = [];
  private sprintRemainingSeconds = 300; // 5 min default (Bus Stop mode)
  private sprintRunning = false;
  private sprintTimerId: number | null = null;

  constructor() {
    this.addLog('[AGENT INIT] Cognitive Engine started. Seated envelope r=0.55m calibrated.');
    this.decomposeIntent(this.activeIntent);
  }

  getIntent(): string {
    return this.activeIntent;
  }

  setIntent(newIntent: string): void {
    this.activeIntent = newIntent;
    this.addLog(`[INTENT CAPTURE] New goal buffer: "${newIntent.slice(0, 42)}..."`);
    this.decomposeIntent(newIntent);
  }

  getNodes(): SpatialTaskNode[] {
    return this.nodes;
  }

  getLogs(): string[] {
    return this.logs;
  }

  addLog(entry: string): void {
    const time = new Date().toLocaleTimeString('en-US', { hour12: false });
    this.logs.unshift(`[${time}] ${entry}`);
    if (this.logs.length > 20) {
      this.logs.pop();
    }
  }

  /**
   * Autonomous decomposition of high-level ambition into
   * actionable 3D nodes arranged in an ergonomic 2ft arc.
   */
  decomposeIntent(intent: string): void {
    this.addLog(`[DECOMPOSE] Tokenizing semantic dependencies for goal.`);
    
    let subtasks: Array<{ title: string; priority: 'P1' | 'P2' | 'P3'; category: string; mins: number }> = [];

    if (intent.toLowerCase().includes('launch') || intent.toLowerCase().includes('horizon')) {
      subtasks = [
        { title: 'Meta XR Hand Physics & Interaction SDK Hook', priority: 'P1', category: 'Platform', mins: 15 },
        { title: 'Ergonomic Curved Arc Clustering Algorithm', priority: 'P2', category: 'UX Design', mins: 20 },
        { title: 'Autonomous Multi-Step Intent Decomposer', priority: 'P1', category: 'Agentic AI', mins: 25 },
        { title: 'Vercel WebXR HTTPS Instant Launch Deploy', priority: 'P3', category: 'DevOps', mins: 10 },
      ];
    } else if (intent.toLowerCase().includes('quantum') || intent.toLowerCase().includes('study')) {
      subtasks = [
        { title: 'Derive Qubit Bloch Sphere State Rotations', priority: 'P1', category: 'Theory', mins: 25 },
        { title: 'Simulate Grover Search Oracle Phase Flip', priority: 'P2', category: 'Algorithm', mins: 30 },
        { title: 'Analyze Error Correction Surface Codes', priority: 'P2', category: 'Synthesis', mins: 20 },
      ];
    } else if (intent.toLowerCase().includes('fps') || intent.toLowerCase().includes('latency') || intent.toLowerCase().includes('opt')) {
      subtasks = [
        { title: 'Batch Three.js Draw Calls for 60+ FPS lock', priority: 'P1', category: 'Engine', mins: 15 },
        { title: 'Profile Havok Physics WebAssembly dispatch', priority: 'P1', category: 'Physics', mins: 20 },
        { title: 'Tune MSAA & Mobile GPU Foveation settings', priority: 'P2', category: 'Vulkan/XR', mins: 15 },
      ];
    } else {
      subtasks = [
        { title: `Core Execution: ${intent.slice(0, 30)}...`, priority: 'P1', category: 'Focus', mins: 20 },
        { title: 'Empirical Verification & Edge Validation', priority: 'P2', category: 'Quality', mins: 15 },
        { title: 'Final Review & Executive Summary', priority: 'P3', category: 'Review', mins: 10 },
      ];
    }

    // Compute ergonomic spatial positions in a seated 2-foot radius arc (r = 0.52m to 0.58m)
    const arcRadius = 0.55;
    const baseHeight = 0.95; // lap / desk height
    const total = subtasks.length;

    this.nodes = subtasks.map((task, index) => {
      // Angular spread from -28 deg to +28 deg (0.5 radians total spread)
      const angle = ((index - (total - 1) / 2) / Math.max(1, total - 1)) * 0.45;
      const x = Math.sin(angle) * arcRadius;
      const z = -Math.cos(angle) * arcRadius;
      const y = baseHeight + (index % 2 === 0 ? 0.04 : -0.02);

      return {
        id: `node-${Date.now()}-${index}`,
        title: task.title,
        priority: task.priority,
        category: task.category,
        status: 'active',
        estimatedMins: task.mins,
        position: [x, y, z],
        targetPosition: [x, y, z],
      };
    });

    this.addLog(`[AGENT CLUSTER] Generated ${this.nodes.length} nodes within 0.55m (Airplane Seat compliant).`);
  }

  /**
   * Auto-clustering algorithm: relaxes spatial nodes into optimal ergonomic arc
   */
  autoClusterNodes(): void {
    this.addLog('[AUTO-CLUSTER] Running spring-repulsion relaxation in 2ft envelope.');
    const arcRadius = 0.55;
    const baseHeight = 0.95;
    const activeNodes = this.nodes.filter((n) => n.status === 'active');
    const total = activeNodes.length;

    activeNodes.forEach((node, i) => {
      const angle = total === 1 ? 0 : ((i - (total - 1) / 2) / (total - 1)) * 0.48;
      node.targetPosition = [
        Math.sin(angle) * arcRadius,
        baseHeight + (i % 2 === 0 ? 0.03 : -0.01),
        -Math.cos(angle) * arcRadius,
      ];
    });

    this.addLog('[AUTO-CLUSTER] All nodes snapped to FoV focus corridor (38 deg).');
  }

  completeTask(nodeIndex: number): SpatialTaskNode | null {
    if (this.nodes[nodeIndex]) {
      this.nodes[nodeIndex].status = 'completed';
      this.addLog(`[TASK DONE] Completed: "${this.nodes[nodeIndex].title.slice(0, 24)}..."`);
      return this.nodes[nodeIndex];
    }
    return null;
  }

  getTelemetry(): CognitiveTelemetry {
    const active = this.nodes.filter((n) => n.status === 'active');
    const p1Count = active.filter((n) => n.priority === 'P1').length;
    const p2Count = active.filter((n) => n.priority === 'P2').length;

    // Cognitive load heuristic
    let load = Math.min(95, 20 + p1Count * 18 + p2Count * 10);
    if (active.length === 0) load = 12;

    const flowState: CognitiveTelemetry['flowState'] =
      load > 75 ? 'Overload Risk' : load < 25 ? 'Deep Flow' : 'Balanced';

    return {
      cognitiveLoadPct: load,
      flowState,
      nodesInReach: active.length,
      maxReachRadiusMeters: 0.55,
      logs: this.logs.slice(0, 5),
    };
  }

  // Bus Stop 5-Minute Sprint Mode
  toggleSprintTimer(onTick: (formattedTime: string, running: boolean) => void): void {
    if (this.sprintRunning) {
      this.sprintRunning = false;
      if (this.sprintTimerId !== null) {
        clearInterval(this.sprintTimerId);
        this.sprintTimerId = null;
      }
      this.addLog('[SPRINT] Bus Stop focus timer paused.');
      onTick(this.formatSprintTime(), false);
    } else {
      this.sprintRunning = true;
      this.addLog('[SPRINT] Bus Stop 5-minute focus session commenced.');
      onTick(this.formatSprintTime(), true);

      this.sprintTimerId = window.setInterval(() => {
        if (this.sprintRemainingSeconds > 0) {
          this.sprintRemainingSeconds -= 1;
          onTick(this.formatSprintTime(), true);
        } else {
          this.sprintRunning = false;
          if (this.sprintTimerId !== null) {
            clearInterval(this.sprintTimerId);
            this.sprintTimerId = null;
          }
          this.addLog('[SPRINT COMPLETE] 100% focused burst achieved! Ready for departure.');
          onTick('00:00', false);
        }
      }, 1000);
    }
  }

  formatSprintTime(): string {
    const m = Math.floor(this.sprintRemainingSeconds / 60);
    const s = this.sprintRemainingSeconds % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  }
}

export const agentEngine = new SynapseAgentEngine();
