/**
 * SynapseDesk AI - Component Definitions
 */

import { defineComponents } from '@iwsdk/core';
import { Robot } from './robot-component.js';
import { SpatialNodeTag, SynapseCoreTag } from './synapse-core.js';

export default defineComponents([Robot, SynapseCoreTag, SpatialNodeTag]);
