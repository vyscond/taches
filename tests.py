from taches import run

run('ls', alias='listing dir', silent=False)
run('cd', alias='change dir')
run('touch testing_taches.txt', alias='touching file')
run('rm testing_taches.txt', alias='removing file')
