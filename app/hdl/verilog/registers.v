// Synthesizable Verilog HDL Shift Registers
module universal_shift_reg_4bit (input wire clk, input wire rst_n, input wire [1:0] mode, input wire [3:0] par_in, input wire s_right, input wire s_left, output reg [3:0] q);
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            q <= 4'b0000;
        else begin
            case (mode)
                2'b00: q <= q; // Hold
                2'b01: q <= {s_right, q[3:1]}; // Shift Right
                2'b10: q <= {q[2:0], s_left};  // Shift Left
                2'b11: q <= par_in;            // Load
            endcase
        end
    end
endmodule

module sipo_buffer_stage_1 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_2 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_3 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_4 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_5 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_6 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_7 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_8 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_9 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_10 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_11 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_12 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_13 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_14 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_15 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_16 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_17 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_18 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_19 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_20 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_21 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_22 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_23 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_24 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_25 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_26 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_27 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_28 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_29 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_30 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_31 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_32 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_33 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_34 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_35 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_36 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_37 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_38 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_39 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_40 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_41 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_42 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_43 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_44 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_45 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_46 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_47 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_48 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_49 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_50 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_51 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_52 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_53 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_54 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_55 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_56 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_57 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_58 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_59 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_60 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_61 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_62 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_63 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_64 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_65 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_66 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_67 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_68 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_69 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_70 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_71 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_72 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_73 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_74 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_75 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_76 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_77 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_78 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_79 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_80 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_81 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_82 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_83 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_84 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_85 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_86 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_87 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_88 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule

module sipo_buffer_stage_89 (input wire clk, input wire serial_in, output reg [7:0] parallel_out);
    always @(posedge clk)
        parallel_out <= {parallel_out[6:0], serial_in};
endmodule
