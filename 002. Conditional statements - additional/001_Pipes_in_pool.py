pool_volume = int(input())
debit_pipe_1 = int(input())
debit_pipe_2 = int(input())
hours = float(input())

volume_from_pipe_1 = debit_pipe_1 * hours
volume_from_pipe_2 = debit_pipe_2 * hours

volume_filled = volume_from_pipe_2 + volume_from_pipe_1

if pool_volume >= volume_filled:
    print(f"The pool is {(volume_filled/pool_volume)*100 :.2f}% full. Pipe 1: {(volume_from_pipe_1/volume_filled)*100 :.2f}%. Pipe 2: {(volume_from_pipe_2/volume_filled)*100 :.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {volume_filled-pool_volume :.2f} liters.")