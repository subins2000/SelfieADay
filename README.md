# SelfieADay

My "selfie a day" hobby files

## Requirements

* The awesome [Photo A Day Aligner](https://github.com/matthewearl/photo-a-day-aligner) tool

## Run

* Copy pictures to `input` folder
* Run `make-input.py`. This'll resize every images in `input` folder to a square which [solves this](https://github.com/matthewearl/photo-a-day-aligner/issues/1)
* Edit `pada.conf` according to your need
* Run :
  ```python3 pada.py align```