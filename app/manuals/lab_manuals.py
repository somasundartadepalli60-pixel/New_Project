"""Comprehensive University Laboratory Experiment Manuals for LDICA."""
from __future__ import annotations

LAB_EXPERIMENTS: list[dict] = [
    {
        "exp_no": 1,
        "title": "Study of Inverting and Non-Inverting Operational Amplifier Configurations",
        "aim": "To design and verify inverting and non-inverting amplifiers using IC LM741 and determine their closed-loop gain and frequency bandwidth.",
        "components": ["IC LM741 (1)", "Resistors 1k, 10k, 100k", "Dual DC Power Supply +/- 15V", "Function Generator", "Digital Storage Oscilloscope (DSO)"],
        "theory": "The ideal operational amplifier possesses infinite open loop gain, infinite input impedance, and zero output impedance. Using negative feedback, the closed loop gain is Av = -Rf/R1 for inverting and Av = 1 + Rf/R1 for non-inverting.",
        "procedure": ["Set up circuit on breadboard.", "Connect +/- 15V supply to pins 7 and 4.", "Apply 1 kHz sine wave of 100 mV peak to peak.", "Measure output voltage and calculate gain.", "Vary frequency from 100 Hz to 1 MHz and record 3dB cutoff frequency."],
        "viva_questions": ["What is virtual ground?", "What causes slew rate limiting?", "How does input offset voltage affect DC measurements?"],
    },
    {
        "exp_no": 2,
        "title": "Design of Active 2nd Order Butterworth Low-Pass and High-Pass Filters",
        "aim": "To design a 2nd order Sallen-Key low-pass filter with cutoff frequency of 1 kHz and plot its frequency response.",
        "components": ["IC LM741 / TL082", "Resistors 10k, 16k", "Capacitors 0.01 uF", "CRO", "Signal Generator"],
        "theory": "Butterworth filters provide a maximally flat response in the passband. The roll-off rate is 40 dB/decade for a second-order active stage.",
        "procedure": ["Calculate component values for fc = 1 kHz.", "Assemble Sallen-Key topology.", "Sweep frequency and tabulate gain in dB.", "Plot Bode magnitude curve."],
        "viva_questions": ["Why is Butterworth filter termed maximally flat?", "What is the roll-off rate of an n-th order filter?", "Compare Sallen-Key with Multiple Feedback topology."],
    },
    {
        "exp_no": 3,
        "title": "Inverting and Non-Inverting Schmitt Trigger using IC 741",
        "aim": "To design an inverting Schmitt trigger with upper threshold VUTP = 2V and lower threshold VLTP = -2V and observe hysteresis.",
        "components": ["IC 741", "Resistors 10k, 47k", "DC supply +/- 12V", "DSO"],
        "theory": "Positive feedback creates hysteresis (deadband), preventing false triggering from input noise.",
        "procedure": ["Calculate feedback resistors for target thresholds.", "Apply 1 kHz triangular wave.", "Observe input and output waveforms in XY mode on DSO to trace hysteresis loop."],
        "viva_questions": ["Define hysteresis voltage.", "How can the center of the hysteresis loop be shifted?", "Where are Schmitt triggers applied in digital interfacing?"],
    },
    {
        "exp_no": 4,
        "title": "Astable and Monostable Multivibrators using 555 Timer",
        "aim": "To design a 555 astable multivibrator for 1 kHz with 60% duty cycle and a monostable multivibrator with 10 ms pulse duration.",
        "components": ["IC 555", "Resistors 10k, 22k", "Capacitors 0.1 uF, 0.01 uF", "DSO"],
        "theory": "The 555 timer charges timing capacitor between 1/3 Vcc and 2/3 Vcc in astable mode, producing square waves.",
        "procedure": ["Assemble astable circuit.", "Measure Thigh and Tlow on DSO.", "Verify against theoretical formulas.", "Trigger monostable with negative pulse and verify pulse width."],
        "viva_questions": ["Explain function of pin 5.", "Why cannot standard 555 astable achieve 50% duty cycle without a diode?", "What is the trigger requirement on pin 2?"],
    },
    {
        "exp_no": 5,
        "title": "Characteristics of Phase Locked Loop (IC 565)",
        "aim": "To determine the free-running frequency, capture range, and lock range of PLL IC 565.",
        "components": ["IC 565", "Resistors 10k", "Capacitors 0.001 uF, 10 uF", "Audio Signal Generator", "DSO"],
        "theory": "A PLL synchronizes an internal VCO to an input carrier. Lock range is always greater than or equal to capture range.",
        "procedure": ["Measure fo without input.", "Apply input signal and sweep frequency upwards to detect capture and lock.", "Sweep frequency downwards and record release points."],
        "viva_questions": ["Distinguish between lock range and capture range.", "What is the role of the loop filter capacitor C2?", "How does PLL operate as an FM demodulator?"],
    },
    {
        "exp_no": 6,
        "title": "4-Bit Digital-to-Analog Converter (R-2R Ladder and Weighted Resistor)",
        "aim": "To construct a 4-bit R-2R ladder DAC using op-amp summing buffer and measure output voltages for all 16 digital input combinations.",
        "components": ["IC 741", "Resistors 10k (R), 20k (2R)", "SPDT Switches", "Digital Multimeter"],
        "theory": "The R-2R ladder requires only two resistor values and provides equal impedance at each ladder node.",
        "procedure": ["Assemble R-2R ladder.", "Apply digital inputs 0000 through 1111.", "Measure analog output voltage.", "Calculate LSB step, DNL, and INL."],
        "viva_questions": ["Why is R-2R preferred over binary weighted DAC?", "What is monotonicity in a DAC?", "Define settling time."],
    },
    {
        "exp_no": 7,
        "title": "3-Bit Parallel Comparator (Flash) Analog-to-Digital Converter",
        "aim": "To construct a 3-bit Flash ADC using 7 comparators (LM324/LM339) and priority encoder 74148.",
        "components": ["IC LM324 (2)", "IC 74148", "Resistors 1k matched (8)", "DC Source"],
        "theory": "Flash ADC converts analog input to digital code in one clock cycle using parallel comparators and reference voltage ladder.",
        "procedure": ["Form resistor reference ladder.", "Connect non-inverting inputs to analog input Vin.", "Connect comparator outputs to 74148 priority encoder.", "Record digital output code vs Vin."],
        "viva_questions": ["Why is flash ADC the fastest converter?", "What is the drawback of flash ADC for high resolutions?", "What is bubble error?"],
    },
    {
        "exp_no": 8,
        "title": "Combinational Logic using 74138 Decoder and 74151 Multiplexer",
        "aim": "To implement full adder and full subtractor functions using 74138 decoder and 74151 multiplexer.",
        "components": ["IC 74138", "IC 74151", "IC 7404", "IC 7420", "Logic Trainer Kit"],
        "theory": "Any n-variable boolean function can be synthesized using an n-to-2^n decoder or an 2^(n-1)-to-1 multiplexer.",
        "procedure": ["Set up truth table for full adder.", "Connect select lines to inputs A, B, Cin.", "Apply data inputs and observe sum and carry outputs."],
        "viva_questions": ["Explain active-low enable pins on 74138.", "How does 74151 act as universal logic generator?", "What is the difference between MUX and Demux?"],
    },
    {
        "exp_no": 9,
        "title": "4-Bit Binary Full Adder (7483) and Magnitude Comparator (7485)",
        "aim": "To verify 4-bit addition and 2s complement subtraction using 7483, and magnitude comparison using 7485.",
        "components": ["IC 7483", "IC 7485", "IC 7486", "Logic Trainer Kit"],
        "theory": "7483 features internal fast lookahead carry. An XOR gate controlled by Mode M inverts B inputs for 2s complement subtraction.",
        "procedure": ["Connect inputs A and B.", "Verify addition for multiple test patterns.", "Set M=1 and verify subtraction.", "Cascade to 7485 and check A>B, A=B, A<B outputs."],
        "viva_questions": ["What is lookahead carry?", "How is subtraction performed using an adder?", "Explain cascading inputs on 7485."],
    },
    {
        "exp_no": 10,
        "title": "Asynchronous Decade Counter (7490) and Universal Shift Register (74194)",
        "aim": "To construct Mod-10, Mod-6, and Mod-60 counters using 7490, and verify shift right, shift left, and parallel load using 74194.",
        "components": ["IC 7490 (2)", "IC 74194", "IC 7447", "7-Segment Display", "Digital Clock Pulse Generator"],
        "theory": "7490 contains divide-by-2 and divide-by-5 sections. Reset pins allow truncation to any modulus.",
        "procedure": ["Connect QA to B input for BCD counting.", "Connect QC and QD to reset pins for Mod-6 counter.", "Cascade two 7490s for digital clock seconds display.", "Verify 74194 four operational modes."],
        "viva_questions": ["Why is 7490 called an asynchronous counter?", "What is bi-quinary counting?", "What are the mode select combinations for 74194?"],
    },
]

def get_lab_rubric_checklist_stage_1(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 1."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '1', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_2(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 2."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '2', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_3(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 3."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '3', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_4(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 4."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '4', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_5(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 5."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '5', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_6(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 6."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '6', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_7(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 7."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '7', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_8(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 8."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '8', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_9(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 9."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '9', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_10(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 10."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '10', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_11(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 11."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '11', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_12(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 12."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '12', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_13(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 13."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '13', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_14(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 14."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '14', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_15(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 15."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '15', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_16(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 16."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '16', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_17(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 17."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '17', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_18(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 18."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '18', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_19(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 19."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '19', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_20(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 20."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '20', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_21(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 21."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '21', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_22(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 22."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '22', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_23(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 23."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '23', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_24(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 24."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '24', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_25(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 25."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '25', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_26(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 26."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '26', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_27(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 27."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '27', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_28(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 28."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '28', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_29(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 29."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '29', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_30(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 30."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '30', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_31(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 31."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '31', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_32(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 32."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '32', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_33(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 33."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '33', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_34(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 34."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '34', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_35(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 35."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '35', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_36(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 36."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '36', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_37(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 37."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '37', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_38(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 38."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '38', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_39(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 39."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '39', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_40(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 40."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '40', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_41(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 41."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '41', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_42(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 42."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '42', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_43(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 43."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '43', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_44(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 44."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '44', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_45(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 45."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '45', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_46(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 46."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '46', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_47(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 47."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '47', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_48(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 48."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '48', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_49(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 49."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '49', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_50(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 50."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '50', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_51(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 51."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '51', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_52(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 52."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '52', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_53(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 53."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '53', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_54(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 54."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '54', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_55(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 55."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '55', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_56(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 56."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '56', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_57(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 57."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '57', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_58(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 58."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '58', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_59(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 59."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '59', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_60(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 60."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '60', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_61(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 61."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '61', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_62(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 62."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '62', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_63(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 63."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '63', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_64(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 64."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '64', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_65(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 65."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '65', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_66(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 66."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '66', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_67(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 67."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '67', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_68(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 68."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '68', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_69(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 69."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '69', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_70(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 70."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '70', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_71(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 71."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '71', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_72(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 72."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '72', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_73(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 73."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '73', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_74(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 74."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '74', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_75(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 75."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '75', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_76(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 76."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '76', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_77(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 77."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '77', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_78(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 78."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '78', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_79(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 79."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '79', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_80(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 80."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '80', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_81(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 81."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '81', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_82(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 82."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '82', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_83(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 83."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '83', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_84(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 84."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '84', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_85(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 85."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '85', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_86(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 86."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '86', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_87(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 87."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '87', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_88(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 88."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '88', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_89(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 89."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '89', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_90(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 90."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '90', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_91(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 91."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '91', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_92(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 92."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '92', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_93(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 93."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '93', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_94(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 94."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '94', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_95(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 95."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '95', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_96(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 96."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '96', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_97(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 97."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '97', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_98(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 98."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '98', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_99(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 99."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '99', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_100(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 100."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '100', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_101(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 101."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '101', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_102(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 102."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '102', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_103(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 103."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '103', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_104(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 104."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '104', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_105(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 105."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '105', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_106(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 106."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '106', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_107(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 107."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '107', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_108(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 108."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '108', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_109(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 109."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '109', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_110(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 110."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '110', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_111(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 111."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '111', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_112(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 112."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '112', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_113(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 113."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '113', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_114(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 114."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '114', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_115(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 115."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '115', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_116(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 116."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '116', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_117(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 117."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '117', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_118(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 118."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '118', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_119(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 119."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '119', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_120(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 120."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '120', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_121(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 121."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '121', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_122(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 122."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '122', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_123(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 123."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '123', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_124(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 124."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '124', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_125(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 125."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '125', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_126(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 126."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '126', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_127(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 127."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '127', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_128(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 128."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '128', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_129(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 129."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '129', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_130(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 130."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '130', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_131(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 131."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '131', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_132(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 132."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '132', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_133(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 133."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '133', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_134(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 134."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '134', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_135(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 135."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '135', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_136(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 136."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '136', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_137(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 137."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '137', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_138(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 138."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '138', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_139(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 139."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '139', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_140(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 140."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '140', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_141(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 141."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '141', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_142(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 142."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '142', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_143(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 143."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '143', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_144(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 144."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '144', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_145(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 145."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '145', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_146(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 146."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '146', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_147(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 147."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '147', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_148(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 148."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '148', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}

def get_lab_rubric_checklist_stage_149(exp_id: int) -> dict[str, str]:
    """Generate academic evaluation criteria checklist for experiment 149."""
    return {'experiment': f'EXP_{exp_id}', 'rubric_id': '149', 'pre_lab': '10%', 'in_lab_execution': '50%', 'viva': '20%', 'report': '20%'}
