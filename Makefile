JOBS=$(shell echo `nproc`)
QEMU_CONFIGURE_FLAGS=--target-list=tricore-softmmu --python=python2
BU_CONFIGURE_FLAGS=--target=tricore --prefix=$(shell pwd)/tricore-binutils/install/
NUMRUNS=100

help:
	@echo "Usage: make { qemu | tests | clean | tools}"

qemu: qemu/build.ok

tools:
	@echo "Building Binutils..."
	@rm -rf tricore-binutils/build/
	@rm -rf tricore-binutils/install/
	@mkdir -p tricore-binutils/build/
	@mkdir -p tricore-binutils/install
	@cd tricore-binutils/build && ../configure $(BU_CONFIGURE_FLAGS) && make -j$(JOBS) && make install

qemu/build.ok:
	@echo "Building QEMU..."
	@rm -rf qemu/build/
	@mkdir -p qemu/build/
	@cd qemu/build && ../configure $(QEMU_CONFIGURE_FLAGS) && make -j$(JOBS) && touch ../build.ok

tests: qemu
	@cd random-insn-test && ./GenerateTests.py $(NUMRUNS)

clean:
	rm -rf qemu/build qemu/build.ok
	rm -rf tricore-binutils/build/ tricore-binutils/install
