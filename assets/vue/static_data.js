const apiUrls = {
  institutions: '/api/institutions/',
  policyCategories: '/api/policy-categories/',
  messageTemplates: '/api/message-templates/',
  contactMessage: '/api/contact/message/',
};

const messageTemplateKind = {
  POSITIVE: 1,
  NEUTRAL: 2,
  NEGATIVE: 3,
};

const socialMediaLinkKind = {
  FACEBOOK: 1,
  INSTAGRAM: 2,
  TWITTER: 3,
  LINKEDIN: 4,
  YOUTUBE: 5,
  WEBSITE: 6,
  ANOTHER: 7,
};


export { apiUrls, messageTemplateKind, socialMediaLinkKind };