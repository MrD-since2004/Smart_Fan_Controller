vlib work
vmap work work

vlog pwm_generator.v
vlog tb_pwm_generator.v

vsim -c work.tb_pwm_generator -do "run -all; quit"
