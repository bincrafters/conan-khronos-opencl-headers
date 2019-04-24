#define CL_TARGET_OPENCL_VERSION 220
#include <CL/cl.h>

int main() {
	return !(CL_VERSION_2_2 == 1);
}
