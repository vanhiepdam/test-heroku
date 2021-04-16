const dev = {
    BASE_API_URL: 'https://hiep-todo.herokuapp.com'
};

const prod = {
    BASE_API_URL: 'https://hiep-todo.herokuapp.com'
};
const config = process.env.REACT_APP_STAGE === 'prod'
  ? prod
  : dev;

export default {
  // Add common config values here
  ...config
};

