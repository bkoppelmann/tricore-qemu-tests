JOBS=$(shell echo `nproc`)
QEMU_CONFIGURE_FLAGS=--target-list=tricore-softmmu --python=python2
NUMRUNS=100

help:
	@echo "Usage: make { qemu | tests | clean }"

qemu: qemu/build.ok

qemu/build.ok:
	@echo "Building QEMU..."
	@rm -rf qemu/build/
	@mkdir -p qemu/build/
	@cd qemu/build && ../configure $(QEMU_CONFIGURE_FLAGS) && make -j$(JOBS) && touch ../build.ok

tests: qemu
	@cd random-insn-test && ./GenerateTests.py $(NUMRUNS)

clean:
	rm -rf qemu/build qemu/build.ok
