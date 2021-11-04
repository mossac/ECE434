#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

#define P9_11   (0x1<<30)
#define P9_31   (0x3<<14)
volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {


	uint32_t *gpio1 = (uint32_t *)GPIO1;
	uint32_t *gpio0 = (uint32_t *)GPIO0;
	uint32_t *gpio3 = (uint32_t *)GPIO3;
	uint32_t gpio = P9_27;
	
	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	while(1){
		gpio1[GPIO_SETDATAOUT]   = USR1;			// The the USR3 LED on
		gpio1[GPIO_CLEARDATAOUT] = USR2;
		gpio3[GPIO_SETDATAOUT] = P9_31;
		gpio0[GPIO_SETDATAOUT] = P9_11;
		
		__R30 |= gpio;		// Set the GPIO pin to 1

		__delay_cycles(0);    // Wait 1/2 second

		gpio1[GPIO_CLEARDATAOUT] = USR1;
        gpio1[GPIO_SETDATAOUT]   = USR2;
		gpio3[GPIO_CLEARDATAOUT] = P9_31;
		gpio0[GPIO_CLEARDATAOUT] = P9_11;
		
		__R30 &= ~gpio;		// Clearn the GPIO pin

		__delay_cycles(0); 

	}
	__halt();
}

// Turns off triggers
#pragma DATA_SECTION(init_pins, ".init_pins")
#pragma RETAIN(init_pins)
const char init_pins[] =  
	"/sys/class/leds/beaglebone:green:usr1/trigger\0none\0" \
	"/sys/class/leds/beaglebone:green:usr2/trigger\0none\0" \
	"/sys/class/gpio/export\0 110\0" \
	"/sys/class/gpio/gpio110/direction\0out\0" \
	"\0\0";
