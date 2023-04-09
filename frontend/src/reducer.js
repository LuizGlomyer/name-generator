import { useReducer } from 'react';

const initialState = {
  loading: false,
  snackbar: false,
  quantity: 1,
  generatedQuantity: 0,
  activeTab: "brazillianName",
  radioSelection: {
    brazillianName: null,
    englishName: null
  },
  items: {
    brazillianName: {},
    englishName: {},
    fantasyName: {}
  }
};

function reducer(state, action) {
  switch (action.type) {
    case "loadingTrue":
      return { ...state, loading: true }
    case "loadingFalse":
      return { ...state, loading: false }
    case "snackbarOpen":
      return { ...state, snackbar: true }
    case "snackbarClose":
      return { ...state, snackbar: false }
    case "updateQuantity": {

      return { ...state, quantity: action.value }
    }
    case "setGeneratedQuantity": {
      return { ...state, generatedQuantity: action.value }
    }
    case "setRadioSelection": {
      const key = action.tab;
      const radioSelection = { ...state.radioSelection };
      radioSelection[key] = action.value
      return { ...state, radioSelection }
    }
    case "setItems": {
      const key = action.tab;
      const items = { ...state.items };
      items[key] = action.value
      return { ...state, items }
    }
    case "setActiveTab": {
      return { ...state, activeTab: action.value }
    }

  }
}

export const getReducer = () => {
  return useReducer(reducer, initialState);
}