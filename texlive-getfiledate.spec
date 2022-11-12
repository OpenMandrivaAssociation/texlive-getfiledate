Name:		texlive-getfiledate
Version:	16189
Release:	1
Summary:	Find the date of last modification of a file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/getfiledate
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/getfiledate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/getfiledate.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package fetches from the system the date of last
modification or opening of an existing file, using the function
\pdffilemoddate (present in recent versions of PDFTeX); the
user may specify how the date is to be presented.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/getfiledate/getfiledate.sty
%doc %{_texmfdistdir}/doc/latex/getfiledate/README
%doc %{_texmfdistdir}/doc/latex/getfiledate/getfiledate-guide.pdf
%doc %{_texmfdistdir}/doc/latex/getfiledate/getfiledate-guide.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
