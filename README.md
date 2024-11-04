# How Many Trucks

## What is it?

How Many Trucks is a project to help shippers plan out their freight operations. By answering a few simple questions, and uploading a list of cargo dimensions, our program can optimize the number of trucks needed to ship the freight. It will even show the optimized way to load the freight.
You start with a list of items you would like loaded onto a truck, a packing sheet, and what type of equipment you want it loaded on to (Van or Flatbed). From there it puts each item through the algorithm and determines what truck the item will go on, and where it will go.

It even tells you if certain items won't fit on any truck.

## How does it do this?

Our program is using advanced optimization techniques developed by researchers to help solve the 3-dimensional bin packing problem. This problem is not a solved one, so there is no proof that there is an "objectively correct" answer, but this program does give you a good answer and does it quickly.

## Setup

In order to run this you need a module that was modified for the shipper's use case, found here: https://github.com/jibarnhart/3dbinpacking. The module it was branched from was a Python implementation of the algorithm described in the paper "Optimizing Three-Dimensional Bin Packing Through Simulation", by Dube and Kanavathy. The main issue with the model (and algorithm), in the shipper's use case, is that is assumes you can tilt items on their side and rotate them whatever way you want to. For now, we have removed this and only allow turning items 90 degrees.

## Shortcomings

Anyone in freight can tell you that the total weight of the trailer is not the only thing that matters. The weights over the front and rear axle are important as well. This program does not yet take those weights into account, but I plan on implementing those in the future.
