import PropTypes from 'prop-types';
import { css } from 'react-emotion';
import { Headset } from '@material-ui/icons';

// import colours from '../constants/colours';

const typeMap = {
  Podcast: Headset,
  // 'White Paper':
};

const icon = css`
  margin-right: 5px;
`;

const ResourceIcon = ({ type }) => {
  const Icon = typeMap[type];

  return !!Icon && <Icon color="action" css={icon} />;
};

ResourceIcon.propTypes = {
  type: PropTypes.string.isRequired,
};

export default ResourceIcon;
