# How Many Trucks

## What is it?

How Many Trucks is a project to help shippers plan out their freight operations. By answering a few simple questions, and uploading a list of cargo dimensions, our program can optimize the number of trucks needed to ship the freight. It will even show the optimized way to load the freight.

## How does it do this?

Our program is using advanced optimization techniques developed by researchers to help solve the 3-dimensional bin packing problem. This problem is not a solved one, so there is no proof that there is an "objectively correct" answer, but this program does give you a good answer and does it quickly.

## Setup

In order to run this you need a module that was modified for the shipper's use case, found here: https://github.com/jibarnhart/3dbinpacking. The module it was branched from was a Python implementation of the algorithm described in the paper "Optimizing Three-Dimensional Bin Packing Through Simulation", by Dube and Kanavathy. The main issue with the model (and algorithm), in the shipper's use case, is that is assumes you can tilt items on their side and rotate them whatever way you want to. For now, we have removed this and only allow turning items 90 degrees.

