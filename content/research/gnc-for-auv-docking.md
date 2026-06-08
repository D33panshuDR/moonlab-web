---
title: GNC for AUV Docking
tagline: Guidance Navigation and Control strategies and algorithms for Autonomous Underwater  Vehicles
featured: true
image: /images/research/hero_image_new_edited3(2).png
summary: Persistent underwater operations rely on Autonomous Underwater Vehicles (AUVs) to periodically offload data and recharge for extended mission endurance. Autonomous docking presents an effective solution for meeting these operational demands. However, successful docking requires the vehicle to approach the dock at a minimum relative speed to avoid physical damage, while taking the effects of varying ocean currents and vehicle buoyancy into account. In this paper, we pose the docking problem as a path-following problem and propose a novel Polynomial-Logarithmic Adaptive Trajectory (PLATO) law that dynamically prescribes the desired velocity to the AUV while meeting the relative speed constraints. The decoupling of the docking problem into path following and the velocity profile controller enables the generalization of the formulation to accommodate different combinations of path-following algorithms and velocity profile controllers. Simulation results validate the proposed approach, demonstrating its effectiveness across various path-following guidance laws and diverse current conditions.
weight: 100
tags:
  - Autonomous Underwater Vehicles (AUV)
  - Underwater Docking
  - Guidance Navigation and Control (GNC)
  - Marine Robotics
---

This project includes development of a robust Guidance, Navigation, and Control suite and architecture to autonomously guide and dock AUVs into a dock. The experiments include simulations in 2D and 3D environments with stationary and moving docks. The AUV used primarily for the results is Girona 500 and the simulator is based on the open source Stonefish simulator.
![](/images/research/Blank%20diagram%281%29.png "GNC suite for AUV docking using a two phase approach and Geometric + Visual Guidance and PLATO speed controller.")

![](/images/research/StoneFish_Simulator_new.png "Stonefish simulator with Girona 500 AUV heading towards the dock with a dashboard displaying mission parameters and a camera output.")
