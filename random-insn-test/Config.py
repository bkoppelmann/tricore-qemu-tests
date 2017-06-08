############################
##
##  Config
##
###########################

tas     = "tricore-as"
tgcc    = "tricore-gcc"
tld     = "tricore-ld"

tsim = "tsim"
qemu = "../../qemu/build/tricore-softmmu/qemu-system-tricore"
version ="161"

ldscript = "target.ld"

baseJumpReg = 14
baseMemReg = 15

maxInsnPerTest = 2000

