export function getUrlId() {
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

export function retrievePathName(menuCats, id) {
  for(let i = 0; i < menuCats.length; i++) {
    let menuCat = menuCats[i];
    if (menuCat.id === id) {
      return menuCat.name;
    }
    let subMenus = menuCat.children;
    if (subMenus !== undefined) {
      for(let j = 0; j < subMenus.length; j++) {
        let subMenu = subMenus[j];
        if (subMenu.id === id) {
          return menuCat.name + " / " + subMenu.name;
        }
      }
    }
  }
  return "";
};

function currencyFormat(number) {
  let curr = number.toLocaleString('vn-VN', { style: 'currency', currency: 'VND' });
  return curr.replace("₫", "");
}

export function getPriceString(min, max) {
  let price = "Liên hệ";
  let priceMin = min * 1000;
  let priceMax = max * 1000;
  if (priceMin !== 0 && priceMax !== 0) {
    price = currencyFormat(priceMin);
    if (priceMax > priceMin) {
      price = price + " - " + currencyFormat(priceMax);
    }
    price = price + " VND";
  }
  return price;
}
