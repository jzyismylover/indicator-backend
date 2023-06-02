import hanlp
from hanlp.utils.torch_util import gpus_available

# torch.multiprocessing.set_start_method('spawn')

if gpus_available():  # 建议在GPU上运行XLMR_BASE，否则运行mini模型
    UNIVERSAL_HANLP = hanlp.load(
        hanlp.pretrained.mtl.UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_XLMR_BASE
    )
    # UNIVERSAL_HANLP = hanlp.load(
    #     hanlp.pretrained.mtl.UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_MMINILMV2L6
    # )
else:
    UNIVERSAL_HANLP = hanlp.load(
        hanlp.pretrained.mtl.UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_MMINILMV2L6
    )

tasks = ['tok', 'ud']
for task in list(UNIVERSAL_HANLP.tasks.keys()):
    if task not in tasks:
        del UNIVERSAL_HANLP[task]
