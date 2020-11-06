import React from 'react';
import ReactDOM from 'react-dom';

import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';
import Collapse from '@material-ui/core/Collapse';
import ExpandMore from '@material-ui/icons/ExpandMore';

import { Provider, connect } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';

import axios from 'axios';
import axiosMiddleware from 'redux-axios-middleware';

import {
  BrowserRouter as Router,
  Route,
  Switch,
  //Link,
  withRouter
} from 'react-router-dom';

import { IS_LOCALHOST, MAIN_DATA } from './common/conf_debug.js';


function getUrlId() {
  let loc = window.location.toString();
  for(let i = loc.length - 1; i >= 0; i--) {
    if (loc.charAt(i) === '#') {
      let idStr = loc.substring(i+1, loc.length);
      let id = parseInt(idStr, 10);
      if (isNaN(id)) {
        id = 0;
      }
      return id;
    }
  }
  return 0;
}

function CategoryMenu(props) {
  //const { match, location, history } = props;
  const { history } = props;
  const [target, setTarget] = React.useState("");

  const onNavigate = function(id) {
    /* Product menu items */
    if ((id > 10 && id < 100) || ([3, 4].includes(id))) {
      //alert('Product');
      history.push('/cat#' + id.toString())
    }
    /* Articles menu items */
    if ((id > 1000) || ([100].includes(id))) {
      //alert('Articles');
      history.push('/art#' + id.toString())
    }
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
  let cats = props.cat === undefined ? [] : props.cat;
  let n = cats.length;
  for(let i = 0; i < n; i++) {
    let menuItem = cats[i];
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
  height: "120px",
  padding: "1rem 0rem 0rem 0rem"
}


const reducer = IS_LOCALHOST ?
  (state = 0, action) => {
    switch (action.type) {
      case "LOAD_CATS_FAIL":
        alert(JSON.stringify(action));
        return Object.assign(
          {},
          state,
          {
          }
        );

      case "LOAD_CATS_SUCCESS":
        //alert(JSON.stringify(action.payload.data));
        //for (let x in MAIN_DATA.products) alert(x);
        //alert(Object.keys(MAIN_DATA.products))
        return Object.assign(
          {},
          state,
          {
            isInit: true,
            menuCategories: MAIN_DATA.productCategories
          }
        );
      default:
        return state;
    }
  } :
  (state = 0, action) => {
    switch (action.type) {
      case "LOAD_CATS_FAIL":
        alert(JSON.stringify(action));
        return Object.assign(
          {},
          state,
          {
          }
        );

      case "LOAD_CATS_SUCCESS":
        //alert(JSON.stringify(action.payload.data));
        //alert(JSON.parse(action.payload.data.content));
        return Object.assign(
          {},
          state,
          {
            isInit: true,
            menuCategories: (JSON.parse(action.payload.data.content)).productCategories
          }
        );
      default:
        return state;
    }
  };

const client = IS_LOCALHOST ?
  axios.create({
    baseURL: "http://localhost:3000/",
    responseType: 'text'
  }) : 
  axios.create({
    baseURL: "https://www.googleapis.com/blogger/v3/blogs/",
    responseType: 'json'
  });

const dispatchToPropsAppMap = IS_LOCALHOST ?
  dispatch => {
    return {
      loadCategory: () => {
          dispatch(
            {
              type: "LOAD_CATS",
              payload: {
                request: {
                  method: "GET",
                  url: "/8396047075318857173/posts",
                  data: {
                  }
                }
              } 
            }
          )
      }
    }
  } : 
  dispatch => {
    return {
      loadCategory: () => {
          dispatch(
            {
              type: "LOAD_CATS",
              payload: {
                request: {
                  method: "GET",
                  url: "/8396047075318857173/posts/9047017506441401269/?key=AIzaSyDskPUFJo9WZqlU2wR09MuRJD8rSVDimDA",
                  data: {
                  }
                }
              } 
            }
          )
      }
    }
  };

const stateToPropsAppMap = (state) => {
   return {
      menuCategories: state.menuCategories,
      isInit: state.isInit
   };
};

const dispatchToPropsProductsMap = null;

const stateToPropsProductsMap = (state) => {
   return {
      menuCategories: state.menuCategories,
      isInit: state.isInit
   };
};

const AboutMe = function(props) {
  return <h2>Trang web đang được xây dựng.</h2>;
}

const Articles = function(props) {
  return <h2>Bai Viet {getUrlId()}</h2>;
}

const Category = connect(stateToPropsProductsMap, dispatchToPropsProductsMap)(
  function(props) {
    return <h2>San pham {getUrlId()}</h2>;
  }
);

const CategoryMenuWithRouter = withRouter(CategoryMenu);

const App = connect(stateToPropsAppMap, dispatchToPropsAppMap)(
  function (props) {
    if (!props.isInit && typeof props.loadCategory === "function") {
      props.loadCategory();
    }
    return (
      <Router>
          <div style={headerContent}><header>
              <h1><center>Cá Kiểng Phong Thủy</center></h1>
              <nav>
              </nav>
          </header></div>

          <div style={flexContainer}>
              <div style={sidebarMenu}><aside>
                  <CategoryMenuWithRouter cat={props.menuCategories} />
              </aside></div>
              <div style={mainContent}>
                  <main>
                    <Switch>
                        <Route path="/art" component={Articles} />
                        <Route path="/cat" component={Category} />
                        <Route path="/" component={AboutMe} />
                    </Switch>
                  </main>
              </div>
          </div>
          <div>
              <footer>
                  <p>&nbsp;</p>
                  <p><center>
                      Copyright © 2020 by Cá Kiểng Phong Thủy
                      - All Rights Reserved.
                  </center></p>
                  <p><center>
                      31 ĐX087, Phường Hiệp An,
                      TP Thủ Dầu Một, Tỉnh Bình Dương -
                      Điện thoại: (+84) 0778 081 441
                  </center></p>
                  <p>&nbsp;</p>
              </footer>
          </div>
      </Router>
    );
  }
);

const store = createStore(
    reducer,
    {
      isInit: false
    },
    applyMiddleware(
      axiosMiddleware(client)
    )
);


ReactDOM.render(
  <Provider store = {store}>
      <App />
  </Provider>,
  document.getElementById('aquarium_store')
);


