import PropTypes from 'prop-types';
import { css } from 'react-emotion';
import { Book, FormatAlignLeft, Headset, ImportContacts, WebRounded } from '@material-ui/icons';

const typeMap = {
  Podcast: Headset,
  Book,
  Website: WebRounded,
  'White Paper': FormatAlignLeft,
  Article: ImportContacts,
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
