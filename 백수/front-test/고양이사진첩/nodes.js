function Nodes({$app,initalstate,onClick}){
    this.state = initalstate

    this.$target = document.createElement('nav')
    this.$target.className = 'Breadcrumb'
    $app.appendChild(this.$target)

    this.onClick = onClick;
    this.render = () => {
        if(this.state.nodes){
            const nodesTemplate = this.state.nodes.map(node=>{
                const path = node.type === 'DIRECTORY' ? './assets/directory.png' : './assets/file.png';

                return`
                    <div class="Node" node-id="${node.id}">
                        <img src="${path}"/>
                        <div>${node.name}</div>
                    </div>
                `
            }).join('')
            this.$target.innerHTML = !this.state.isRoot ? `<div class="Node"><img src="/assets/prev.png"></div>${nodesTemplate}` : nodesTemplate
        }

        this.$target.querySelectorAll('.Node').forEach($node => {
            $node.addEventListener('click', (e) => {
              // dataset을 통해 data-로 시작하는 attribute를 꺼내올 수 있음
              const { nodeId } = e.target.dataset
              const selectedNode = this.state.nodes.find(node => node.id === nodeId)
    
              if (selectedNode) {
                this.onClick(selectedNode)
              }
            })
        })
    }
    this.setState = nextState => {
        this.state = nextState
        this.render()
    }
}

export default Nodes;