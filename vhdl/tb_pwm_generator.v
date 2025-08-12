`timescale 1ns/1ps

module tb_pwm_generator;

    reg clk = 0;
    reg [7:0] duty = 8'd128; // Default 50%
    wire pwm_out;

    // Parameters to control simulation run
    reg [31:0] sim_time_ns = 1000000000; // 1 second default simulation time
    reg [7:0] custom_duty = 8'd128;      // Default duty 50%
    
    pwm_generator uut (
        .clk(clk),
        .duty(duty),
        .pwm_out(pwm_out)
    );

    // Clock: 100 MHz
    always #5 clk = ~clk;

    initial begin
        // Start with default duty
        duty = 8'd128;
        $display("Simulation started with default duty: %d", duty);

        // Wait a bit before applying custom duty
        #100;

        // Apply custom duty for sim_time_ns
        $display("Applying custom duty: %d for %0dns", custom_duty, sim_time_ns);
        duty = custom_duty;
        #(sim_time_ns);

        // Revert to default duty
        duty = 8'd128;
        $display("Simulation for %0dns done. Reverting to default duty: %d", sim_time_ns, duty);

        // Keep simulation running
        #10000000;
        $finish;
    end

endmodule
