from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'results.json').read_text());out=ROOT/'assets'
BLUE='#287bb5';GRAY='#bac5ce';INK='#273442';ORANGE='#df8c49'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.edgecolor':'#cbd5de','axes.labelcolor':INK,'xtick.color':'#5d6b77','ytick.color':INK,'svg.fonttype':'none','figure.facecolor':'white','axes.facecolor':'white'})
def save(fig,name):
 fig.savefig(out/f'{name}.svg',bbox_inches='tight',pad_inches=.18,metadata={'Date':None});plt.close(fig)
def hbars(key,name,col=-1,xlim=100):
 rows=D[key]['rows'];f,a=plt.subplots(figsize=(9,3.5 if len(rows)<7 else 4.3))
 y=np.arange(len(rows));v=[r[col] for r in rows];colors=[GRAY]*(len(rows)-1)+[BLUE]
 a.barh(y,v,color=colors,height=.54);a.set_yticks(y,[r[0] for r in rows]);a.invert_yaxis();a.set_xlim(0,xlim);a.set_axisbelow(True);a.xaxis.grid(True,color='#eaf0f3');a.tick_params(axis='y',length=0)
 for i,x in enumerate(v):a.text(x+1,i,f'{x:.2f}',va='center',color=BLUE if i==len(rows)-1 else INK,weight='bold' if i==len(rows)-1 else 'normal')
 a.set_xlabel('Average Recall@1 (%)' if key=='retrieval' else 'Average success rate (%)');f.tight_layout();save(f,name)
hbars('retrieval','retrieval',xlim=100);hbars('rlbench','rlbench',xlim=60)
f,axs=plt.subplots(1,3,figsize=(11,3.1));rows=D['ablation']['rows']
for j,(a,title,lim) in enumerate(zip(axs,['Visual retrieval','Latent-action retrieval','Code-agreement gap'],[100,45,40]),1):
 vals=[r[j] for r in rows];a.barh(range(5),vals,color=[BLUE]+[GRAY]*4,height=.55);a.invert_yaxis();a.set_xlim(0,lim);a.set_title(title,fontsize=11,pad=14);a.set_yticks(range(5),[r[0] for r in rows] if j==1 else ['']*5);a.tick_params(axis='y',length=0);a.xaxis.grid(True,color='#eaf0f3');a.set_axisbelow(True)
 for i,v in enumerate(vals):a.text(v+.5,i,f'{v:.2f}',va='center',fontsize=9)
f.tight_layout();save(f,'ablation')
f,axs=plt.subplots(1,2,figsize=(10,3.5));rows=list(reversed(D['scaling']['rows']));x=np.arange(3)
for col,label,color in [(1,'Visual R@1',BLUE),(2,'Latent R@1',ORANGE)]:
 axs[0].plot(x,[r[col] for r in rows],'-o',color=color,lw=2.5,label=label)
 for i,r in enumerate(rows):axs[0].annotate(f'{r[col]:.2f}',(i,r[col]),xytext=(0,10),textcoords='offset points',ha='center',fontsize=10)
axs[0].set_ylim(0,100);axs[0].set_ylabel('Recall@1 (%)');axs[0].legend(frameon=False,loc='center right')
v=[r[4] for r in rows];axs[1].bar(x,v,color=['#a9c9df','#70a9cf',BLUE],width=.45);axs[1].set_ylim(0,5);axs[1].set_ylabel('CALVIN average sequence length')
for i,y in enumerate(v):axs[1].text(i,y+.12,f'{y:.3f}',ha='center',color=INK)
for a in axs:a.set_xticks(x,['5%','25%','100%']);a.set_xlabel('Fraction of paired data');a.grid(axis='y',color='#eaf0f3');a.set_axisbelow(True)
f.tight_layout();save(f,'scaling')
f,a=plt.subplots(figsize=(9,4.3));rows=D['calvin']['rows'];colors=['#b1b8c1','#857ca7','#c4a785','#94b6a1','#4e9fa2','#cd91b1','#e9ad72',BLUE]
for i,r in enumerate(rows):a.plot(range(1,6),r[1:6],'-o',label=r[0],color=colors[i],lw=3 if i==7 else 1.5,markersize=6 if i==7 else 4)
a.set_xticks(range(1,6));a.set_ylim(0,105);a.set_xlim(.8,5.2);a.set_xlabel('Consecutive tasks completed');a.set_ylabel('Success rate (%)');a.yaxis.grid(True,color='#eaf0f3');a.legend(frameon=False,bbox_to_anchor=(1.01,1),loc='upper left',fontsize=10)
f.tight_layout();save(f,'calvin')
f,a=plt.subplots(figsize=(9,3.6));x=np.arange(4);width=.22
for j,(idx,color) in enumerate([(1,'#a59bb8'),(4,'#70a9ac'),(7,BLUE)]):
 r=D['realworld']['rows'][idx];v=r[1:5];xx=x+(j-1)*width;a.bar(xx,v,width,color=color,label=r[0])
 for xx1,y in zip(xx,v):a.text(xx1,y+1.5,f'{y:.1f}',ha='center',fontsize=9)
a.set_xticks(x,['Pick','Push','Press','Flip']);a.set_ylim(0,105);a.set_ylabel('Success rate (%)');a.yaxis.grid(True,color='#eaf0f3');a.set_axisbelow(True);a.legend(frameon=False,ncol=3,loc='upper center',bbox_to_anchor=(.5,1.18));f.tight_layout();save(f,'realworld')
print('Created six result charts')
