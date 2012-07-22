# PyMite Configuration

CC=i586-elf-gcc
AR=i586-elf-ar

PLATFORM := $(notdir $(CURDIR))
PM_LIB_ROOT = pmvm_$(PLATFORM)
PM_LIB_FN = lib$(PM_LIB_ROOT).a
PM_LIB_PATH = ../../vm/$(PM_LIB_FN)
PM_USR_SOURCES = main.py
PM_HEAP_SIZE = 0x2000
PMIMGCREATOR := ../../tools/pmImgCreator.py
PMGENPMFEATURES := ../../tools/pmGenPmFeatures.py
IPM = true
DEBUG = true

SOURCES = plat.c
OBJS = $(SOURCES:.c=.o)

ifeq ($(DEBUG),true)
	CDEFS += -g -ggdb -D__DEBUG__=1
endif
CINCS = -I$(abspath .)
CFLAGS = -c -m32 -nostdlib -fno-builtin -nostartfiles -nodefaultlibs -I../../vm $(CDEFS) $(CINCS)

export CFLAGS IPM PM_LIB_FN

.PHONY: all clean

all : pmfeatures.h $(OBJS) $(PM_LIB_PATH)

$(PM_LIB_PATH) : ../../vm/*.c ../../vm/*.h
	make -C ../../vm

pmfeatures.h : pmfeatures.py $(PMGENPMFEATURES)
	$(PMGENPMFEATURES) pmfeatures.py > $@

clean :
	$(MAKE) -C ../../vm clean
	$(RM) $(TARGET).out $(OBJS) $(TARGET)_img.* $(TARGET)_nat.* pmfeatures.h
