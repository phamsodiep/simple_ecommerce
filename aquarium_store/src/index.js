import React from 'react';
import ReactDOM from 'react-dom';

import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';
import Collapse from '@material-ui/core/Collapse';
import ExpandMore from '@material-ui/icons/ExpandMore';

import { Provider, connect } from 'react-redux';
import { createStore } from 'redux';


const catsTree = {
  "root": [
    {
      "id": 0,
      "name": "Sản phẩm"
    },
    {
      "id": 1,
      "name": "Cá",
      "hasProducts": true,
      "children": [
        {
          "id": 11,
          "name": "Cá chép",
          "children": [
          ]
        },
        {
          "id": 12,
          "name": "Cá dĩa",
          "children": [
          ]
        },
        {
          "id": 13,
          "name": "Cá rồng",
          "children": [
          ]
        },
      ]
    },
    {
      "id": 2,
      "name": "Cây thủy sinh",
      "children": [
      ]
    },
    {
      "id": 3,
      "name": "Động vật khác",
      "children": [
      ]
    },
    {
      "id": 4,
      "name": "Thức ăn",
      "children": [
      ]
    },
    {
      "id": 5,
      "name": "Hồ - đèn - bơm - lọc",
      "children": [
      ]
    },
    {
      "id": 6,
      "name": "Dụng cụ",
      "children": [
      ]
    },
    {
      "id": 7,
      "name": "Linh tinh",
      "children": [
        {
          "id": 71,
          "name": "Trang trí",
          "children": [
          ]
        },
        {
          "id": 72,
          "name": "Thuốc và hóa chất",
          "children": [
          ]
        }
      ]
    },

    {
      "id": 0,
      "name": "Bài viết"
    },
    {
      "id": 100,
      "name": "Hướng dẫn setup",
      "children": [
      ]
    },
    {
      "id": 200,
      "name": "Mẹo",
      "children": [
        {
          "id": 201,
          "name": "Mẹo chăm sóc",
          "children": [
          ]
        },
        {
          "id": 202,
          "name": "Mẹo phong thủy",
          "children": [
          ]
        }
      ]
    }
  ]
};


function CategoryMenu(props) {
  const [target, setTarget] = React.useState("");

  const onNavigate = typeof props.onNavigate === "function" ? props.onNavigate :
    function(id) {
      //alert(id);
    };

  const headingStyle = {
    background: "#F3F3F3"
  }

  const groupStyle = {
    background: "#D0D0D0"
  }

  const itemStyle = {
    paddingLeft: "34px",
    background: "#E0E0E0",
  }

  const createClickHandler = function (id) {
    return () => {
      setTarget(id);
      onNavigate(id);
    };
  }
  
  const createNavigatingHandler = function (id) {
    return () => {
      onNavigate(id)
    }
  }

  let items = [];

  let n = props.cat.root.length;
  for(let i = 0; i < n; i++) {
    let menuItem = props.cat.root[i];
    /* Menu group name heading */
    if (menuItem.id === 0) {
      items[items.length] = (
          <React.Fragment>
              <ListItem style={headingStyle}>
                  <ListItemText primary={menuItem.name} />
              </ListItem>
          </React.Fragment>
      );
      continue;
    }
    let m = menuItem.children.length;
    /* Menu item with sub menu item */
    if (m > 0) {
      let subItems = []
      for (let j = 0; j < m; j++) {
        let menuSubItem = menuItem.children[j]
        subItems[subItems.length] = (
          <ListItem button style={itemStyle} onClick={createNavigatingHandler(menuSubItem.id)}>
              <ListItemText primary={menuSubItem.name} />
          </ListItem>
        );
      }
      items[items.length] = (
          <React.Fragment>
              <ListItem button onClick={createClickHandler(menuItem.id)} style={groupStyle}>
                  <ListItemText primary={menuItem.name} />
                  {target === menuItem.id ? "" : <ExpandMore />}
              </ListItem>
              <Collapse in={target === menuItem.id}>
                  <List component="div" disablePadding>
                      {subItems}
                  </List>
              </Collapse>
              <Divider light/>
          </React.Fragment>
      );
    }
    /* Menu item without sub menu item */
    else {
      items[items.length] = (
          <React.Fragment>
              <ListItem button onClick={createClickHandler(menuItem.id)} style={groupStyle}>
                  <ListItemText primary={menuItem.name} />
              </ListItem>
              <Divider light/>
          </React.Fragment>
      );
    }
  }

  return (
    <List component="nav">
        {items}
    </List>
  );
}

const onNavigating = (id) => {
  //alert('id = ' + id);
}

const flexContainer = {
  display: "flex",
  justifyContent: "space-between"
}

const sidebarMenu = {
  minWidth: "13em",
  padding: "0px 10px 0px 10px",
  borderRadius: "10px",
  border: "1px solid black",
  margin: "0rem 1rem 0rem 1rem"
}

const mainContent = {
  width: "100%",
}

const headerContent = {
  height: "120px"
}

const dispatchToPropsAppMap = dispatch => {
  return {
    loadCategory: () => {
        dispatch({})
    }
  }
}

const App = connect(null, dispatchToPropsAppMap)(
  function (props) {
    return (
      <React.Fragment>
          <div style={headerContent}><header>
              <h1><center>Cá Kiểng Phong Thủy</center></h1>
              <nav>
              </nav>
          </header></div>

          <div style={flexContainer}>
              <div style={sidebarMenu}><aside>
                  <CategoryMenu cat={catsTree} onNavigate={onNavigating}/>
              </aside></div>
              <div style={mainContent}>
                  <main>
                      <h2>Trang web đang được xây dựng.</h2>
                  </main>
                  <footer>
                      <p>© cakiengphongthuy.blogspot.com</p>
                  </footer>
              </div>
          </div>
      </React.Fragment>
    );
  }
);

const reducer = (state = 0, action) => {
  switch (action.type) {
    default:
      return state;
  }
};

const store = createStore(
    reducer,
    {
    }
);


ReactDOM.render(
  <Provider store = {store}>
      <App />
  </Provider>,
  document.getElementById('aquarium_store')
);


