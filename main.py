import sys

from problems.dna import run_dna
from problems.rna import run_rna
from problems.revc import run_revc
from problems.gc import run_gc
from problems.hamm import run_hamm
from problems.subs import run_subs
from problems.prot import run_prot
from problems.fib import run_fib
from problems.iprb import run_iprb
from problems.fibd import run_fibd
from problems.mrna import run_mrna
from problems.iev import run_iev
from problems.cons import run_cons
from problems.grph import run_grph
from problems.mprt import run_mprt
from problems.orf import run_orf

problems = {
    'dna': run_dna,
    'rna': run_rna,
    'revc': run_revc,
    'gc': run_gc,
    'hamm': run_hamm,
    'subs': run_subs,
    'prot': run_prot,
    'fib': run_fib,
    'iprb': run_iprb,
    'fibd': run_fibd,
    'mrna': run_mrna,
    'iev': run_iev,
    'cons': run_cons,
    'grph': run_grph,
    'mprt': run_mprt,
    'orf': run_orf,
}

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('''Usage:

python3 %s <problem_code> < dataset.txt > output.txt
''' % sys.argv[0])
        sys.exit(1)

    problem = problems.get(sys.argv[1])
    if not problem:
        print(
            'Couldn\'t find "{}" problem. Available ones:\n{}',
            sys.argv[1],
            '\n'.join(sorted(problems)))
        sys.exit(1)

    inpt = sys.stdin.read().strip()
    print(problem(inpt))
