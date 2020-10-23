import ReactDOM from 'react-dom';
import React from 'react';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';
import Collapse from '@material-ui/core/Collapse';
import ExpandMore from '@material-ui/icons/ExpandMore';

const catsTree = {
  "root": [
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
    }
  ]
};


function CategoryMenu(props) {
  const [target, setTarget] = React.useState("");

  const onNavigate = typeof props.onNavigate === "function" ? props.onNavigate :
    function(id) {
      //alert(id);
    };

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
    let m = menuItem.children.length;
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
              <Divider />
          </React.Fragment>
      );
    }
    else {
      items[items.length] = (
          <React.Fragment>
              <ListItem button onClick={createClickHandler(menuItem.id)} style={groupStyle}>
                  <ListItemText primary={menuItem.name} />
              </ListItem>
              <Divider />
          </React.Fragment>
      );
    }
  }

  return (
    <List component="nav">
        <Divider />
        {items}
    </List>
  );
}

const onNavigating = (id) => {
  alert('id = ' + id);
}

ReactDOM.render(
  <React.Fragment>
      <CategoryMenu cat={catsTree} onNavigate={onNavigating}/>
  </React.Fragment>,
  document.getElementById('material_ui_entry')
);

