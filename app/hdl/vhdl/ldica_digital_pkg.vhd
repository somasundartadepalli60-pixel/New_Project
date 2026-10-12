-- VHDL Digital Package Declarations
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

package ldica_digital_pkg is
    type logic_array_t is array (natural range <>) of std_logic_vector(7 downto 0);
    function compute_parity(data : std_logic_vector) return std_logic;
end package ldica_digital_pkg;

package body ldica_digital_pkg is
    function compute_parity(data : std_logic_vector) return std_logic is
        variable par : std_logic := '0';
    begin
        for i in data'range loop
            par := par xor data(i);
        end loop;
        return par;
    end function;
end package body ldica_digital_pkg;
-- Package utility function block 1
-- Package utility function block 2
-- Package utility function block 3
-- Package utility function block 4
-- Package utility function block 5
-- Package utility function block 6
-- Package utility function block 7
-- Package utility function block 8
-- Package utility function block 9
-- Package utility function block 10
-- Package utility function block 11
-- Package utility function block 12
-- Package utility function block 13
-- Package utility function block 14
-- Package utility function block 15
-- Package utility function block 16
-- Package utility function block 17
-- Package utility function block 18
-- Package utility function block 19
-- Package utility function block 20
-- Package utility function block 21
-- Package utility function block 22
-- Package utility function block 23
-- Package utility function block 24
-- Package utility function block 25
-- Package utility function block 26
-- Package utility function block 27
-- Package utility function block 28
-- Package utility function block 29
-- Package utility function block 30
-- Package utility function block 31
-- Package utility function block 32
-- Package utility function block 33
-- Package utility function block 34
-- Package utility function block 35
-- Package utility function block 36
-- Package utility function block 37
-- Package utility function block 38
-- Package utility function block 39
-- Package utility function block 40
-- Package utility function block 41
-- Package utility function block 42
-- Package utility function block 43
-- Package utility function block 44
-- Package utility function block 45
-- Package utility function block 46
-- Package utility function block 47
-- Package utility function block 48
-- Package utility function block 49
-- Package utility function block 50
-- Package utility function block 51
-- Package utility function block 52
-- Package utility function block 53
-- Package utility function block 54
-- Package utility function block 55
-- Package utility function block 56
-- Package utility function block 57
-- Package utility function block 58
-- Package utility function block 59
-- Package utility function block 60
-- Package utility function block 61
-- Package utility function block 62
-- Package utility function block 63
-- Package utility function block 64
-- Package utility function block 65
-- Package utility function block 66
-- Package utility function block 67
-- Package utility function block 68
-- Package utility function block 69
-- Package utility function block 70
-- Package utility function block 71
-- Package utility function block 72
-- Package utility function block 73
-- Package utility function block 74
-- Package utility function block 75
-- Package utility function block 76
-- Package utility function block 77
-- Package utility function block 78
-- Package utility function block 79
