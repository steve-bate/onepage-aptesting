#!/bin/sh

poetry install
cd submodules/onepage.pub
npm install
cd -
