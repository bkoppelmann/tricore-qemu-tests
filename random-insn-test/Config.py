############################
##
##  Config
##
###########################
prefix = "../tricore-binutils/install/bin/"

tas     = prefix + "tricore-as"
tld     = prefix + "tricore-ld"

tsim = "tsim"
qemu = "../../qemu/build/tricore-softmmu/qemu-system-tricore"
version ="13"

ldscript = "target.ld"

baseJumpReg = 14
baseMemReg = 15

maxInsnPerTest = 2000

