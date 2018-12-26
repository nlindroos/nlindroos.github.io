import PropTypes from 'prop-types';
import { ClimbingBoxLoader } from 'react-spinners';
import styled, { css } from 'react-emotion';

import colours from '../constants/colours';

const FullScreenContainer = styled.div`
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;

  background-color: ${colours.backgroundTransparent};
  // justify-content: center;
  // align-items: center;
`;

// const Loader = styled(ClimbingBoxLoader)`
//   position: initial !important;
// `;

const overrided = css`
  // Need to use !important to override react-spinner's css.
  position: initial !important;
`;

// @@TODO Should maybe be inserted in App.js? or somewhere where it's correctly
// positioned even when navigation occurs.
// @@TODO Add a fade-in & fade-out animation
const FullScreenLoader = ({ loading }) =>
  loading && (
    <FullScreenContainer>
      <ClimbingBoxLoader
        className={overrided}
        sizeUnit="vmin"
        size={3}
        color={colours.greenLight}
        // loading={loading}
      />
    </FullScreenContainer>
  );

FullScreenLoader.propTypes = {
  loading: PropTypes.bool.isRequired,
};
export default FullScreenLoader;
