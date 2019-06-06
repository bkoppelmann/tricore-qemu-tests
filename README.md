# tricore-qemu-tests

## Getting started
If you don't have you own version of the tricore binutils, run `make tools` first. This builds the last public code release version, 
however it does not contain TriCore v1.6+ instructions.
If you have your own version you need to add it's path to [Config.py](https://github.com/bkoppelmann/tricore-qemu-tests/blob/master/random-insn-test/Config.py),
as well as changing the version number. Also you might want to add extra instructions to test, to 
[InstructionList.py](https://github.com/bkoppelmann/tricore-qemu-tests/blob/master/random-insn-test/InstructionList.py).

## Running tests
Once you happy with the setup type `NUMRUNS=X make tests`.
