const search = document.querySelector('[data-case-search]');
if (search) {
  const cards = [...document.querySelectorAll('[data-case]')];
  const empty = document.querySelector('[data-search-empty]');
  search.addEventListener('input', () => {
    const terms = search.value.toLowerCase().trim().split(/\s+/);
    let count = 0;
    for (const card of cards) {
      const content = `${card.textContent} ${card.dataset.case}`.toLowerCase();
      card.hidden = !terms.every(term => content.includes(term));
      if (!card.hidden) count++;
    }
    empty.hidden = count > 0;
  });
}

const trends = document.querySelector('[data-trends]');
if (trends) {
  trends.addEventListener('submit', event => {
    event.preventDefault();
    const keyword = new FormData(trends).get('q').trim();
    if (!keyword) return;
    const url = new URL(trends.action);
    url.search = new URLSearchParams({ date: 'today 3-m', q: keyword });
    window.location.assign(url.href);
  });
}

function publicUrl(value) {
  try {
    const url = new URL(value);
    if (url.protocol === 'https:' && !url.username && !url.password) return url;
  } catch { /* Unrecognized reports stay in GitHub. */ }
  return null;
}

function readSubmission(issue) {
  if (issue.pull_request || !issue.body || !issue.user?.login) return null;
  const sections = new Map();
  const parts = issue.body.split(/^### (.+)\r?$/m);
  for (let index = 1; index < parts.length; index += 2) {
    sections.set(parts[index].trim(), parts[index + 1].trim());
  }
  const name = sections.get('项目名 / Project name');
  const website = publicUrl(sections.get('项目公开链接 / Project URL'));
  const logo = publicUrl(sections.get('Logo 图片直链 / Logo image URL'));
  const description = sections.get('一句话介绍 / One-line description');
  const consent = sections.get('自愿公开 / Consent');
  if (!name || !website || !logo || !description || !/^- \[x\] 我用过 logo-brand-designer/im.test(consent || '')) return null;
  website.hash = '';
  return { name: name.slice(0, 80), website, logo, description: description.slice(0, 180), login: issue.user.login };
}

function submissionCard(item) {
  const article = document.createElement('article');
  article.className = 'card card-body';
  const image = document.createElement('img');
  image.className = 'submitted-logo';
  image.alt = item.name + ' Logo';
  image.loading = 'lazy';
  image.referrerPolicy = 'no-referrer';
  image.src = item.logo.href;
  image.addEventListener('error', () => { image.hidden = true; });
  const title = document.createElement('h3');
  const link = document.createElement('a');
  link.href = item.website.href;
  link.textContent = item.name;
  title.append(link);
  const paragraph = document.createElement('p');
  paragraph.textContent = item.description;
  article.append(image, title, paragraph);
  return article;
}

async function loadShowcase(grid) {
  const status = document.querySelector('[data-community-status]');
  try {
    let url = 'https://api.github.com/repos/webkubor/logo-brand-designer/issues?labels=showcase-submission&state=open&per_page=100';
    const projects = new Map();
    while (url) {
      const response = await fetch(url);
      if (!response.ok) throw new Error('GitHub API unavailable');
      for (const issue of await response.json()) {
        const item = readSubmission(issue);
        if (!item) continue;
        const key = item.website.href.replace(/\/$/, '');
        if (!projects.has(key)) projects.set(key, item);
      }
      url = response.headers.get('link')?.match(/<(https:\/\/api\.github\.com\/[^>]+)>;\s*rel="next"/)?.[1];
    }
    const items = [...projects.values()];
    if (!items.length) {
      status.textContent = '社区展台还没有已公开提交的作品。欢迎提交第一件。';
      return;
    }
    grid.replaceChildren(...items.map(submissionCard));
    const users = new Set(items.map(item => item.login.toLowerCase()));
    status.textContent = `${items.length} 个公开提交的项目，来自 ${users.size} 个 GitHub 账号。`;
  } catch {
    status.textContent = '暂时无法从 GitHub 读取作品。你仍可打开 GitHub 查看公开提交。';
  }
}

const showcase = document.querySelector('[data-community]');
if (showcase) loadShowcase(showcase);
