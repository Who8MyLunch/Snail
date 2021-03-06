# PLL index number
PLL_A = 0
PLL_B = 1

# Crystal's internal load capacitance 
XTAL_CL_6PF =  0b01
XTAL_CL_8PF =  0b10
XTAL_CL_10PF = 0b11

XTAL_CL_DEF = XTAL_CL_10PF

# Input clock dividers, Si5351C only
CLKIN_DIV_1 = 0b00
CLKIN_DIV_2 = 0b01
CLKIN_DIV_4 = 0b10
CLKIN_DIV_8 = 0b11

##########################################
# PLL source select
PLL_SRC_XTAL = 0
PLL_SRC_CLKIN = 1  # Si5351C only

PLL_SRC_DEF = PLL_SRC_XTAL

##########################################
# MultiSynth source select
MS_SRC_PLL_A = PLL_A
MS_SRC_PLL_B = PLL_B

MS_SRC_PLL_DEF = MS_SRC_PLL_A

# MS divide by 4
MS_DIVBY4_ENABLE =  0b11
MS_DIVBY4_DISABLE = 0b00

##########################################
# Clock output enable/disable
CLK_OEB_ENABLE =  0
CLK_OEB_DISABLE = 1

# Clock powered
CLK_PDN_ON  = 0
CLK_PDN_OFF = 1

# Clock state when disabled
CLK_DIS_STATE_LOW =      0b00
CLK_DIS_STATE_HIGH =     0b01
CLK_DIS_STATE_HIGH_IMP = 0b10
CLK_DIS_STATE_NEVER =    0b11

# Clock drive current (mA)
CLK_IDRV_2 = 0b00
CLK_IDRV_4 = 0b01
CLK_IDRV_6 = 0b10
CLK_IDRV_8 = 0b11

# Clock source
CLK_SRC_XTAL =  0b00
CLK_SRC_CLKIN = 0b01
CLK_SRC_MS04 =  0b10
CLK_SRC_MS =    0b11

# Clock initial phase offset
CLK_PHOFF_ZERO = 0

# Clock inverted (180 deg phase shift)
CLK_INV_TRUE =  1
CLK_INV_FALSE = 0

# Clock output divider values
R_DIV_1   = 0b000
R_DIV_2   = 0b001
R_DIV_4   = 0b010
R_DIV_8   = 0b011
R_DIV_16  = 0b100
R_DIV_32  = 0b101
R_DIV_64  = 0b110
R_DIV_128 = 0b111

# Fanout enable/disable for CLKIN_FANOUT_EN, XO_FANOUT_EN, and MS_FANOUT_EN
FANOUT_ENABLE =  0b1
FANOUT_DISABLE = 0b0

#-----------------------------------------
if __name__ == '__main__':
    pass
