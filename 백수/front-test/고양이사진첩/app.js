import Breadcrumb from './breadcrumb.js';
import Nodes from './nodes.js';
import {request} from './api.js';

function App($app){
  this.state = {
    isRoot: false,
    nodes: [],
    depth: []
  }

  const breadcrumb = new Breadcrumb({
    $app,
    initialState: this.state.depth
  })
  const nodes = new Nodes({
    $app,
    initialState: {
      isRoot: this.state.isRoot,
      nodes: this.state.nodes
    },

    onClick: (node) => {
      if (node.type === 'DIRECTORY') {
        // DIRECTORY인 경우 처리
        // 여기에서 Breadcrumb 관련 처리를 하게 되면, Nodes에서는 Breadcrumb를 몰라도 됨.
      } else if(node.type === 'FILE') {
        // FILE인 경우 처리
      }
    }
  })

  this.setState = (nextState) => {
    this.state = nextState;
    breadcrumb.setState(this.state.depth)
    nodes.setState({
      isRoot: this.state.isRoot,
      nodes: this.state.nodes,
    })
  }

  const init = async() => {
    try{
      const rootNodes = await request();
      this.setState({
        ...this.state,
        isRoot: true,
        nodes: rootNodes
      })
    } catch(e) {
      console.error(e);
    }
  }

  init();
}

export default App;