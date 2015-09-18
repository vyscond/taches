from taches import run

run('ls tasky', alias='listing dir', silent=False)
run('cd tasky', alias='change dir')
run('touch tasky/inside.py', alias='touching file')
run('rm tasky/inside.py', alias='removing file')