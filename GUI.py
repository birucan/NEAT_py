import tkinter as tk
from Genome import *



class GUI:
    gen=''


    window = tk.Tk()
    window.title("Genome gui")

    canHeight=800
    canWidth=800
    locR=0

    nodeContainer={}
    lineList={}
    selected=-1


    nodeInfo='no node selected'
    NodeData=''



    def helloCallBack(self, nGenome):
        self.setGenome(nGenome)
        self.eraseLines()
        self.drawConnections(nGenome)
        self.drawNodes(self.gen, self.locR)
        self.Canvas.update_idletasks


    Canvas=tk.Canvas(window, bg="white", height=canHeight, width=canWidth);



    def __init__(self, nGenome, r):

        self.locR=r

        self.nodeContainer={}
        self.setGenome(nGenome)
        self.drawConnections(nGenome)
        self.drawNodes(nGenome, r)


        self.Canvas.config(height=self.canHeight+125)

        self.NodeData= tk.Label(self.Canvas,text="test")


        B1 = tk.Button(self.Canvas, text ="Random Weight", command = lambda: self.gen.mutateWeightRandom())
        B2 = tk.Button(self.Canvas, text ="Weight Shift", command = lambda: self.gen.mutateWeightShift())
        B3 = tk.Button(self.Canvas, text ="Link Mutate", command = lambda: self.gen.mutateLink())
        B4 = tk.Button(self.Canvas, text ="Node Mutate", command = lambda: self.gen.mutateNode())
        B5 = tk.Button(self.Canvas, text ="enable/diable", command = lambda: self.gen.mutateToggleLink())
        B6 = tk.Button(self.Canvas, text ="Mutate", command = lambda: self.gen.mutate())
        B7 = tk.Button(self.Canvas, text ="Calculate", command = lambda: self.helloCallBack(nGenome))
        B8 = tk.Button(self.Canvas, text ="render", command = lambda: self.helloCallBack(nGenome))

        B1.place(x=10,y=self.canHeight+50)
        bWidth=B1.winfo_reqwidth()+10
        B2.place(x=bWidth,y=self.canHeight+50)
        bWidth=bWidth+B2.winfo_reqwidth()+5
        B3.place(x=bWidth,y=self.canHeight+50)
        bWidth=bWidth+B3.winfo_reqwidth()+5
        B4.place(x=bWidth,y=self.canHeight+50)
        bWidth=bWidth+B4.winfo_reqwidth()+5
        B5.place(x=bWidth,y=self.canHeight+50)
        bWidth=bWidth+B5.winfo_reqwidth()+5
        B6.place(x=bWidth,y=self.canHeight+50)
        bWidth=bWidth+B6.winfo_reqwidth()+5
        B7.place(x=bWidth,y=self.canHeight+50)

        B8.place(x=0,y=0)


        self.NodeData.place(x=0, y=self.canHeight+25)

        self.Canvas.pack()
        self.window.mainloop()

    def setGenome(self,nGen):
        self.gen=nGen



    def selectNode(self, event):
        curId=event.widget.find_withtag('current')[0]
        if(curId in self.lineList.keys()):
            curId=event.widget.find_withtag('current')[0]
            if(not self.selected == -1):
                self.Canvas.itemconfig(self.selected, fill='#000000')

            self.selected=curId

            self.NodeData.config(text="Selected Innovation: "+str(self.lineList[curId].getInnovationNum())+" Weight: "+str(self.lineList[curId].getWeight())+" Enabled: "+str(self.lineList[curId].isEnabled()))
            #self.NodeData.place(x=self.canWidth/2, y=self.canHeight+25)
            self.Canvas.itemconfig(curId, fill='#00ff29')
        else:
            curId=event.widget.find_withtag('current')[0]
            if(not self.selected == -1):

                self.Canvas.itemconfig(self.selected, fill='#bfbfbf')

            self.selected=curId


            self.NodeData.config(text="Selected Innovation: "+str(self.nodeContainer[curId].getInnovationNum()))
            #self.NodeData.place(x=self.canWidth/2, y=self.canHeight+25)
            self.Canvas.itemconfig(curId, fill='#ff0000')

    def drawNodes(self, gen, r):

        for a in gen.getNodes().List:
            nX=self.canWidth*a.getX()
            nY=(self.canHeight*a.getY())-(self.canHeight+20)

            #print("Draw node in x0,y0,x1,y1:   "+str(nX-r)+" , "+str(nY-r)+" , "+str(nX+r)+" , "+str(nY+r))
            circle = self.Canvas.create_oval(nX-r, nY-r,  nX+r,nY+r , outline="#000000",fill="#bfbfbf", width=1.2)
            #print(circle)
            self.nodeContainer[circle]=a
            self.Canvas.tag_bind(circle,'<ButtonPress-1>', self.selectNode)

    def drawConnections(self, gen):

        for a in gen.getConnections().List:

            if(type(a.getOrigin())==float):
                print(a)
            else:
                #print("From: "+str(a.getOrigin())+" To: "+str(a.getTarget()))

                oX=self.canWidth*a.getOrigin().getX()
                oY=self.canHeight*a.getOrigin().getY()-(self.canHeight+20)

                tX=self.canWidth*a.getTarget().getX()
                tY=self.canHeight*a.getTarget().getY()-(self.canHeight+20)


                #print("creating line from X0,Y0 To X1,Y1  "+str(oX)+","+str(oY)+" To "+str(tX)+","+str(tY))
                if(a.isEnabled()):
                    line= self.Canvas.create_line(oX,oY,tX,tY, fill="#000000",width=1)
                    self.Canvas.tag_bind(line,'<ButtonPress-1>', self.selectNode)
                    self.lineList[line]=a
                else:
                    line= self.Canvas.create_line(oX,oY,tX,tY, fill="#ff0000", width=1)
                    self.Canvas.tag_bind(line,'<ButtonPress-1>', self.selectNode)
                    self.lineList[line]=a

    def eraseLines(self):
        for a in self.lineList:
            self.Canvas.delete(a)

        self.lineList = {}
