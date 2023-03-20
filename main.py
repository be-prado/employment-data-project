import beprado_eda
import jpitti_eda



def main():
    
    beprado_figs = beprado_eda.run_eda_analysis()
    for fig in beprado_figs:
        fig.show()

    jpitti_figs = jpitti_eda.jp_figs()
    for fig in jpitti_figs:
        fig.show()


    return
    

main()