import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.size":11})
out="pags/imagens/"
# Parte A: curva de calibracao
C=np.array([1,2,3,4,5.])          # [KIO3] apos a mistura (10^-3 mol/L)
t=np.array([86.72,42.42,29.64,21.38,18.05])
y=1/t
a,b=np.polyfit(C*1e-3,y,1)
tx=44.61; Cx=(1/tx-b)/a*1e3
fig,ax=plt.subplots(figsize=(7,4.2))
ax.plot(C,y*100,"o",color="#1f4e9c",label="Amostras A a E")
cc=np.linspace(0,5.5,10); ax.plot(cc,(a*cc*1e-3+b)*100,"-",color="#1f4e9c",lw=1,label="Reta ajustada")
ax.plot([Cx],[100/tx],"*",ms=12,color="#c0392b",label=f"Desconhecida ({Cx:.2f}".replace(".",",")+r"$\times10^{-3}$ mol/L)")
ax.plot([0,Cx,Cx],[100/tx,100/tx,0],":",color="#c0392b",lw=1)
ax.set_xlim(0,5.5); ax.set_ylim(0,6.2)
ax.set_xlabel(r"[KIO$_3$] após a mistura ($10^{-3}$ mol/L)"); ax.set_ylabel(r"1/t ($10^{-2}$ s$^{-1}$)")
ax.grid(alpha=.3); ax.legend(fontsize=9,loc="upper left"); fig.tight_layout(); fig.savefig(out+"grafico_calibracao.png",dpi=200)
print(a,b,Cx)
# Parte B: temperatura
T=np.array([5,15,25.]); tt=np.array([59.59,42.47,29.64])
fig,ax=plt.subplots(figsize=(7,4.2))
ax.plot(T,100/tt,"o-",color="#c0392b")
for Ti,ti in zip(T,tt): ax.annotate(f"{ti:.2f} s".replace(".",","),(Ti,100/ti),textcoords="offset points",xytext=(-20,8),fontsize=9)
ax.set_xlabel("Temperatura (°C)"); ax.set_ylabel(r"1/t ($10^{-2}$ s$^{-1}$)"); ax.set_xlim(0,30); ax.set_ylim(1,4)
ax.grid(alpha=.3); fig.tight_layout(); fig.savefig(out+"grafico_temperatura.png",dpi=200)
