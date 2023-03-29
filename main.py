import beprado_eda
import jpitti_eda
import anranyao_eda
import ccrand_eda
import yuxichen_eda


def main():
    
    beprado_figs = beprado_eda.run_eda_analysis()
    for fig in beprado_figs:
        fig.show()

    jpitti_figs = jpitti_eda.jp_figs()
    for fig in jpitti_figs:
        fig.show()

    anranyao_figs = anranyao_eda.run_eda_analysis()
    for fig in anranyao_figs:
        fig.show()
    
    ccrand_figs = ccrand_eda.run_eda_analysis()
    for fig in ccrand_figs:
        fig.show()

    return
    
    yuxichen_figs = yuxichen_eda.run_eda_analysis()
    for fig in yuxichen_figs:
        fig.show()
    
    return

main()
