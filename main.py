import beprado_eda



def main():
    
    beprado_figs = bernardo_eda.run_eda_analysis()
    for fig in beprado_figs:
        fig.show()

    return
    

main()