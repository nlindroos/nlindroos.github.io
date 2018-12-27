import { createMuiTheme } from '@material-ui/core/styles';

import colours from '../constants/colours';

const palette = {
  primary: { main: colours.greenDark },
  secondary: { main: colours.yellowDark },
  typography: {
    useNextVariants: true,
  },
};

export default createMuiTheme({ palette });
