import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.size":11})
ti=np.arange(0,81,20); tp=np.arange(120,401,20)
sets={"B":([23.6,23.7,23.7,23.6,23.7],[26.8,27.9,28.8,29.7,30.4,30.9,31.2,31.3,31.5,31.5,31.5,31.4,31.4,31.3,31.3],8),
      "C":([23.3]*5,[27.6,27.5,27.4,27.4,27.5,27.4,27.4,27.4,27.4,27.5,27.5,27.4,27.4,27.4,27.4],0)}
out="pags/imagens/"
for k,(Ti,Tp,i0) in sets.items():
    fig,ax=plt.subplots(figsize=(7,4.2))
    ax.plot(ti,Ti,"o",color="#1f4e9c",label="Antes da mistura")
    ax.plot(tp,Tp,"s",color="#c0392b",label="Após a mistura")
    m=np.mean(Ti); ax.hlines(m,0,100,colors="#1f4e9c",linestyles="--",label=f"$T_{{inicial}}$ = {m:.2f} °C".replace(".",","))
    a,b=np.polyfit(tp[i0:],Tp[i0:],1); tt=np.linspace(100,400,10)
    Tf=a*100+b
    ax.plot(tt,a*tt+b,"-",color="#c0392b",lw=1,label="Reta de resfriamento (extrapolada)")
    ax.axvline(100,color="gray",ls=":",lw=1); ax.text(103,m+0.3,"mistura\n(t = 100 s)",fontsize=9,color="gray")
    ax.plot([100],[Tf],"*",ms=12,color="k",label=f"$T_{{final}}$ = {Tf:.2f} °C".replace(".",","))
    ax.set_xlabel("t (s)"); ax.set_ylabel("T (°C)"); ax.grid(alpha=.3); ax.legend(fontsize=9,loc="lower right")
    fig.tight_layout(); fig.savefig(out+f"grafico_{k}.png",dpi=200)
