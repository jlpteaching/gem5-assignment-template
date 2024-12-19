# Notes

Note: You need to run the following in gem5/util/m5.

```shell
scons riscv.CROSS_COMPILE=riscv64-linux-gnu- build/riscv/out/libm5.a
scons build/arm64/out/libm5.a
scons build/x86/out/libm5.a
```

Note that all binaries need an md5sum.
