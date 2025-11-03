#!/usr/bin/env python3
# Adaptive Coherence Framework (ACF v1.3 RC-B)
# Minimal illustrative skeleton of the five stabilizing mechanisms.
# License: CC-BY-4.0

from dataclasses import dataclass
import argparse, random

@dataclass
class Agent:
    phase: float       # oscillatory phase
    amplitude: float   # oscillation amplitude
    sensitivity: float # adaptive sensitivity parameter

def refractory_gating(agent: Agent, last_spike: float, t: float, tau: float = 0.2):
    if t - last_spike < tau:
        agent.amplitude *= 0.9
    return agent

def grace_damping(agent: Agent, k: float = 0.02):
    agent.amplitude -= k * agent.amplitude
    return agent

def adaptive_sensitivity(agent: Agent, local_error: float, eta: float = 0.05):
    agent.sensitivity = max(0.0, min(1.0, agent.sensitivity - eta * local_error))
    return agent

def stochastic_coupling(agent: Agent, noise_scale: float = 0.01):
    agent.phase += random.uniform(-noise_scale, noise_scale)
    return agent

def weak_long_range_bridging(agent: Agent, global_bias: float = 0.005):
    agent.phase += global_bias
    return agent

def step(agent: Agent, t: float, last_spike: float, local_error: float):
    refractory_gating(agent, last_spike, t)
    grace_damping(agent)
    adaptive_sensitivity(agent, local_error)
    stochastic_coupling(agent)
    weak_long_range_bridging(agent)
    return agent

def demo(n: int = 8, steps: int = 100):
    agents = [Agent(phase=random.random(), amplitude=1.0, sensitivity=0.5) for _ in range(n)]
    last_spike = 0.0
    for t in range(steps):
        local_error = random.uniform(0, 1)
        for a in agents:
            step(a, t*0.01, last_spike, local_error)
    print(f"Demo finished: {n} agents, {steps} steps")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="run an illustrative demo")
    args = parser.parse_args()
    if args.demo:
        demo()
    else:
        print("ACF core skeleton loaded. Use --demo to run the illustrative loop.")
